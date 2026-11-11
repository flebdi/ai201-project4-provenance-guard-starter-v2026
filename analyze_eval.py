#!/usr/bin/env python3
"""
Score a run_eval.py report against the five criteria in criteria.md.

    python analyze_eval.py results/run_<stamp>_before.md results/extra_<stamp>_before.md

run_eval.py leaves the Verdict column blank on purpose. This reads its saved
JSON and applies each target exactly as criteria.md words it, per trial — a
target has to hold in every trial to be MET.
"""

import json
import re
import statistics
import sys
from pathlib import Path

import config


def trials_by_scenario(path):
    md = Path(path).read_text(encoding="utf-8")
    out = {}
    for name, body in re.findall(r"^### (.+?)\n\n(.*?)(?=^### |\Z)", md, re.S | re.M):
        out[name] = [json.loads(b) for b in re.findall(r"```json\n(.*?)\n```", body, re.S)]
    return out


def main(run_path, extra_path):
    run = trials_by_scenario(run_path)
    extra_md = Path(extra_path).read_text(encoding="utf-8")
    extra = [json.loads(b) for b in re.findall(r"```json\n(.*?)\n```", extra_md, re.S)]

    rows = []

    c1 = [sum(r["guess"] == "ai" for r in t) for t in run["staff human writing"]]
    n1 = len(run["staff human writing"][0])
    rows.append(("1. Plain human writing is not accused", "≤ 1 labelled AI",
                 [f"{x}/{n1} AI" for x in c1], all(x <= 1 for x in c1)))

    c2 = [sum(r["guess"] == "ai" for r in t) for t in run["unedited AI text"]]
    n2 = len(run["unedited AI text"][0])
    rows.append(("2. Obvious AI text still gets caught", f"≥ 5 of {n2} labelled AI",
                 [f"{x}/{n2} AI" for x in c2], all(x >= 5 for x in c2)))

    gaps = []
    for ai_t, hu_t in zip(run["gap: AI set"], run["gap: human set"]):
        gaps.append(statistics.mean(r["confidence"] for r in ai_t)
                    - statistics.mean(r["confidence"] for r in hu_t))
    rows.append(("3. Clearly-AI and clearly-human score far apart", "gap ≥ 0.40",
                 [f"{g:+.3f}" for g in gaps], all(g >= 0.40 for g in gaps)))

    c4 = [(t["criterion_4"]["real_ok"], t["criterion_4"]["fake_ok"]) for t in extra]
    rows.append(("4. An appeal is always recorded", "10/10 real + 5/5 fake",
                 [f"{a}/10 + {b}/5" for a, b in c4], all(a == 10 and b == 5 for a, b in c4)))

    c5_status = [[r["status"] for r in t] for t in run["bad input"]]
    c5_extra = [t["criterion_5"]["fully_ok"] for t in extra]
    c5_5xx = [sum(s is None or s >= 500 for s in st) for st in c5_status]
    rows.append(("5. Bad input never crashes the service", "0 5xx; 8/8 4xx + error + log",
                 [f"{z} 5xx · {f}/8" for z, f in zip(c5_5xx, c5_extra)],
                 all(z == 0 for z in c5_5xx) and all(f == 8 for f in c5_extra)))

    print("| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |")
    print("|---|---|---|---|---|---|")
    for name, target, runs, met in rows:
        print(f"| {name} | {target} | {' | '.join(runs)} | **{'MET' if met else 'MISSED'}** |")

    print("\nPer-text combined scores (trial 1), and whether trials matched:")
    for name, trials in run.items():
        if name == "bad input":
            print(f"  {name}: statuses {c5_status[0]}")
            continue
        scores = [[r["confidence"] for r in t] for t in trials]
        same = all(s == scores[0] for s in scores)
        t1 = trials[0]
        print(f"  {name}: identical across trials: {same}")
        for r in t1:
            print(f"    {r['confidence']:.3f}  model {r['model_score']:.3f}  "
                  f"style {r['style_score']:.3f}  {r['guess']:<6}  {r['sent'][:48]}")
        print(f"    mean {statistics.mean(x['confidence'] for x in t1):.3f}, "
              f"max {max(x['confidence'] for x in t1):.3f}  "
              f"(AI line {config.AI_THRESHOLD})")


if __name__ == "__main__":
    main(*sys.argv[1:3])
