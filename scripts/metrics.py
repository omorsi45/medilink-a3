"""Dashboard metrics for MediLink Release 2.4, from data/github_export.json.

Run scripts/export_github.sh first. Stdlib only.
No lines of code, commit counts or hours. See docs/dashboard.md for what
each number does and doesn't tell you.
"""
import json
import os
import re
import sys
from datetime import datetime
from statistics import median

# Experiment groups (docs/experiment.md)
BEFORE = {11, 12, 13}


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def minutes(a, b):
    return round((ts(b) - ts(a)).total_seconds() / 60, 1)


def first_review_at(pr):
    times = [r["submittedAt"] for r in pr.get("reviews", []) if r.get("submittedAt")]
    return min(times) if times else None


def review_turnaround(pr):
    first = first_review_at(pr)
    return minutes(pr["createdAt"], first) if first else None


def lead_time(pr):
    return minutes(pr["createdAt"], pr["mergedAt"]) if pr.get("mergedAt") else None


def first_time_right(pr):
    """True if no new commits were pushed after the first review."""
    first = first_review_at(pr)
    if first is None:
        return None
    return not any(ts(c["committedDate"]) > ts(first) for c in pr["commits"])


def checklist(pr):
    """(ticked, total) for the DoD checkboxes in the PR body."""
    body = pr.get("body") or ""
    ticked = len(re.findall(r"^- \[x\]", body, re.M | re.I))
    unticked = len(re.findall(r"^- \[ \]", body, re.M))
    return ticked, ticked + unticked


def max_concurrent(prs, now):
    """Most PRs open at the same moment."""
    events = []
    for pr in prs:
        events.append((ts(pr["createdAt"]), 1))
        end = pr.get("mergedAt") or pr.get("closedAt") or now
        events.append((ts(end), -1))
    events.sort(key=lambda e: (e[0], e[1]))
    cur = best = 0
    for _, d in events:
        cur += d
        best = max(best, cur)
    return best


def med(values):
    values = [v for v in values if v is not None]
    return round(median(values), 1) if values else None


def summarize(prs, checks, now):
    merged = [p for p in prs if p.get("mergedAt")]
    ftr = [first_time_right(p) for p in merged]
    ftr = [f for f in ftr if f is not None]
    ticked = sum(checklist(p)[0] for p in merged)
    total = sum(checklist(p)[1] for p in merged)
    with_ci = sum(1 for p in prs if checks.get(str(p["number"]), 0) > 0)
    return {
        "prs": len(prs),
        "merged": len(merged),
        "median_review_turnaround_min": med(review_turnaround(p) for p in prs),
        "median_lead_time_min": med(lead_time(p) for p in merged),
        "first_time_right": f"{sum(ftr)}/{len(ftr)}",
        "dod_checklist": f"{ticked}/{total}",
        "max_open_prs_at_once": max_concurrent(prs, now),
        "ci_on_first_commit": f"{with_ci}/{len(prs)}",
    }


def blocked(issues):
    return [i["number"] for i in issues if i["state"] == "OPEN"
            and any(l["name"] == "blocked" for l in i["labels"])]


def main(path):
    data = json.load(open(path))
    prs, issues = data["prs"], data["issues"]
    checks, now = data["first_commit_checks"], data["exported_at"]
    print(f"Export: {path} (exported {now} UTC)")
    print(f"PRs: {len(prs)}, issues: {len(issues)}\n")
    print("Per PR")
    print(f"{'PR':>4} {'review(min)':>11} {'lead(min)':>9} {'FTR':>5} {'DoD':>5} {'CI 1st':>6}")
    for p in sorted(prs, key=lambda p: p["number"]):
        t, n = checklist(p)
        print(f"{p['number']:>4} {str(review_turnaround(p)):>11} {str(lead_time(p)):>9} "
              f"{str(first_time_right(p)):>5} {t}/{n:<3} {checks.get(str(p['number']), 0):>6}")
    print("\nWhole cycle")
    for k, v in summarize(prs, checks, now).items():
        print(f"  {k}: {v}")
    print(f"  open blocked items: {len(blocked(issues))} {blocked(issues)}")
    print("\nExperiment (docs/experiment.md)")
    before = [p for p in prs if p["number"] in BEFORE]
    after = [p for p in prs if p["number"] not in BEFORE]
    print(f"  before PRs {sorted(p['number'] for p in before)}: {summarize(before, checks, now)}")
    print(f"  after  PRs {sorted(p['number'] for p in after)}: {summarize(after, checks, now)}")


if __name__ == "__main__":
    default = os.path.join(os.path.dirname(__file__), "..", "data", "github_export.json")
    main(sys.argv[1] if len(sys.argv) > 1 else default)
