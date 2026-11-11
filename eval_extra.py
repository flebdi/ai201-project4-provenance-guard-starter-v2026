#!/usr/bin/env python3
"""
The two criteria run_eval.py can't fully test, three trials each.

    python app.py                               # in one terminal
    python eval_extra.py --label before         # in another

Criterion 4 — an appeal is always recorded.
    10 real submissions per trial, each appealed: the appeal must return 200
    AND add a log entry with status `under_review` after the original
    decision. Then 5 appeals with made-up content_ids: each must return 404
    AND add no appeal entry.

Criterion 5 — bad input never crashes the service.
    The 7 bad bodies from scenarios.py plus the one a dict can't express — a
    body that isn't a JSON object. Each must return a 4xx (no 5xx), carry an
    `error` field, AND leave a `rejected` entry in the audit log. run_eval.py
    only sees the status code; this checks the other two halves.

It reads the audit log straight from disk (audit.read_entries), so it must run
on the same machine as the service. Trials are spaced 30 seconds apart so the
requests that carry no creator_id — which count against this machine's
address — stay under the 5-a-minute limit and actually reach the route.
"""

import argparse
import datetime as dt
import json
import time

import requests

import audit
import config
import scenarios

URL = f"http://{config.HOST}:{config.PORT}"

BAD_REQUESTS = [("dict", body) for body in next(
    s["bodies"] for s in scenarios.SCENARIOS if s.get("criterion") == 5
)] + [("not_an_object", [1, 2, 3])]


def criterion_4(trial: int) -> dict:
    real = []
    for i, text in enumerate(scenarios.AI_PARAGRAPHS, 1):
        sub = requests.post(f"{URL}/submit", json={
            "text": text, "creator_id": f"eval_appeal_t{trial}_{i}"}, timeout=90)
        cid = sub.json().get("content_id") if sub.ok else None
        if not cid:
            real.append({"i": i, "submit_status": sub.status_code, "ok": False})
            continue
        app = requests.post(f"{URL}/appeal", json={
            "content_id": cid, "reasoning": "I wrote this myself."}, timeout=30)
        entries = audit.entries_for(cid)
        decision_at = next((n for n, e in enumerate(entries) if e.get("status") == "decided"), None)
        appeal_at = next((n for n, e in enumerate(entries)
                          if e.get("event") == "appeal" and e.get("status") == "under_review"), None)
        ok = (app.status_code == 200 and decision_at is not None
              and appeal_at is not None and appeal_at > decision_at)
        real.append({"i": i, "content_id": cid, "appeal_status": app.status_code,
                     "response_status": app.json().get("status"),
                     "log_order": [e.get("status") for e in entries], "ok": ok})

    fake = []
    for j in range(1, 6):
        cid = f"fake{trial}{j}000000"
        app = requests.post(f"{URL}/appeal", json={
            "content_id": cid, "reasoning": "I wrote this myself."}, timeout=30)
        appeal_entries = [e for e in audit.entries_for(cid) if e.get("event") == "appeal"]
        fake.append({"content_id": cid, "appeal_status": app.status_code,
                     "appeal_entries_logged": len(appeal_entries),
                     "ok": app.status_code == 404 and not appeal_entries})

    return {"real_ok": sum(r["ok"] for r in real), "real_total": len(real),
            "fake_ok": sum(f["ok"] for f in fake), "fake_total": len(fake),
            "real": real, "fake": fake}


def criterion_5() -> dict:
    results = []
    for kind, body in BAD_REQUESTS:
        before = len(audit.read_entries())
        r = requests.post(f"{URL}/submit", json=body, timeout=90)
        new = audit.read_entries()[before:]
        try:
            payload = r.json()
        except ValueError:
            payload = {"_not_json": r.text[:200]}
        rejected = [e for e in new if e.get("status") == "rejected"]
        sent = json.dumps(body)
        results.append({
            "sent": sent if len(sent) <= 80 else sent[:77] + "...",
            "kind": kind,
            "status": r.status_code,
            "error": payload.get("error") if isinstance(payload, dict) else None,
            "rejected_logged": bool(rejected),
            "logged_reason": rejected[0].get("reason") if rejected else None,
            "ok": (400 <= r.status_code < 500 and isinstance(payload, dict)
                   and bool(payload.get("error")) and bool(rejected)),
        })
    return {"no_5xx": sum(r["status"] < 500 for r in results),
            "fully_ok": sum(r["ok"] for r in results), "total": len(results),
            "results": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--pause", type=float, default=30.0,
                        help="seconds between trials (keeps no-creator requests under the limit)")
    parser.add_argument("--start-delay", type=float, default=65.0,
                        help="seconds to wait first, so a run_eval.py run just before "
                             "has left the rate-limit window")
    args = parser.parse_args()

    time.sleep(args.start_delay)
    trials = []
    for t in range(1, args.trials + 1):
        if t > 1:
            time.sleep(args.pause)
        c4 = criterion_4(t)
        c5 = criterion_5()
        trials.append({"trial": t, "criterion_4": c4, "criterion_5": c5})
        print(f"trial {t}: criterion 4 real {c4['real_ok']}/{c4['real_total']}, "
              f"fake {c4['fake_ok']}/{c4['fake_total']} · criterion 5 "
              f"no-5xx {c5['no_5xx']}/{c5['total']}, fully ok {c5['fully_ok']}/{c5['total']}")

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"extra_{stamp}{label}.md"
    lines = [f"# Criteria 4 and 5{f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `eval_extra.py::main` (criterion_4, criterion_5)",
             "- Service: `app.py::appeal`, `app.py::submit` · log: `audit.py`",
             f"- {args.trials} trials · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}", "",
             "| Trial | C4 real appeals recorded | C4 fake ids refused, unlogged "
             "| C5 no 5xx | C5 4xx + error + rejected entry |",
             "|---|---|---|---|---|"]
    for t in trials:
        c4, c5 = t["criterion_4"], t["criterion_5"]
        lines.append(f"| {t['trial']} | {c4['real_ok']}/{c4['real_total']} | "
                     f"{c4['fake_ok']}/{c4['fake_total']} | {c5['no_5xx']}/{c5['total']} | "
                     f"{c5['fully_ok']}/{c5['total']} |")
    lines += ["", "## What actually came back", ""]
    for t in trials:
        lines += [f"### Trial {t['trial']}", "", "```json", json.dumps(t, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
