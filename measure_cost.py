#!/usr/bin/env python3
"""
Measure what one /submit costs — capstone, Milestone 3.

    python app.py                 # in one terminal
    python measure_cost.py        # in another

Nothing here calls a paid API: the model runs on this machine, so the real
cost of a run is seconds of compute. This sends N real paragraphs (the
false-positive and evasion rows of the attack set, which are all genuine
writing), each from its own creator_id so the rate limit never trips, then
reads the server's own `duration_ms` for each one back out of the audit log.

Two numbers per request:
  client_ms  — wall time as the caller sees it (includes HTTP)
  server_ms  — the duration_ms the service logged (inside the request)

Writes results/cost_<date>.md.
"""

import argparse
import csv
import datetime as dt
import statistics
import time
from pathlib import Path

import requests

import config

HERE = Path(__file__).parent
DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"


def load_texts(n: int) -> list[tuple[str, str]]:
    rows = list(csv.DictReader((HERE / "attack_set" / "attacks.csv").open(encoding="utf-8")))
    real = [(r["id"], r["text"]) for r in rows if r["family"] in ("false_positive", "evasion")]
    return (real * (n // len(real) + 1))[:n]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-n", type=int, default=10)
    ap.add_argument("--url", default=DEFAULT_URL)
    ap.add_argument("--label", default="")
    args = ap.parse_args()

    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    texts = load_texts(args.n)
    sent = []
    for i, (tid, text) in enumerate(texts, 1):
        creator = f"cost_{stamp}_{i:02d}"
        t0 = time.perf_counter()
        r = requests.post(f"{args.url}/submit", json={"text": text, "creator_id": creator}, timeout=120)
        client_ms = (time.perf_counter() - t0) * 1000
        body = r.json()
        sent.append({"i": i, "id": tid, "creator": creator, "status": r.status_code,
                     "content_id": body.get("content_id"), "client_ms": client_ms,
                     "chars": len(text)})
        print(f"{i:>2} {tid:<5} {r.status_code} client {client_ms:7.1f} ms")

    log = requests.get(f"{args.url}/log", params={"limit": args.n * 3}, timeout=30).json()["entries"]
    by_creator = {e.get("creator_id"): e for e in log}
    for s in sent:
        s["server_ms"] = (by_creator.get(s["creator"]) or {}).get("duration_ms")

    ok = [s for s in sent if s["status"] == 200 and s["server_ms"] is not None]
    srv = [s["server_ms"] for s in ok]
    cli = [s["client_ms"] for s in ok]

    def summary(xs):
        xs = sorted(xs)
        return (f"mean {statistics.mean(xs):.1f} ms, median {statistics.median(xs):.1f} ms, "
                f"min {xs[0]:.1f} ms, max {xs[-1]:.1f} ms")

    lines = [
        f"# Cost run {stamp} {args.label}".rstrip(),
        "",
        f"{len(ok)} of {len(sent)} requests returned 200 with a logged duration.",
        "",
        "| # | input | chars | status | client_ms | server_ms (logged) |",
        "|---|---|---|---|---|---|",
    ]
    for s in sent:
        srv_s = f"{s['server_ms']:.1f}" if s["server_ms"] is not None else "—"
        lines.append(f"| {s['i']} | {s['id']} | {s['chars']} | {s['status']} | "
                     f"{s['client_ms']:.1f} | {srv_s} |")
    if ok:
        lines += ["", f"- server: {summary(srv)}", f"- client: {summary(cli)}"]
    out = HERE / "results" / f"cost_{stamp}{('_' + args.label) if args.label else ''}.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[-2:]))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
