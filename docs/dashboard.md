# Engineering dashboard: Release 2.4

Numbers come from `scripts/metrics.py`, which reads a gh export of this repo (`scripts/export_github.sh` → `data/github_export.json`). Latest output is saved in `data/metrics_output.txt`.

None of these use lines of code, commit counts or hours online. Every number here is a reason to go look at something, not a verdict on a person.

| # | Metric | What it measures | Why it's useful | What it does NOT prove |
|---|---|---|---|---|
| 1 | Review turnaround (median min) | Time from a PR being opened to its first review | The scenario's PRs sat open for days. This shows if review is the bottleneck | That reviews were good. A fast, shallow review scores well. Here every review is my own, so it isn't the same as a second person's review |
| 2 | PR lead time (median min) | Time from PR opened to merged | Shows how long finished code waits before it's in main | That the work was small or easy, or that the person is fast. A hard bug can rightly take longer |
| 3 | First-Time-Right | Share of merged PRs with no new commits after the first review | Rework found in review costs time. A low rate points at unclear requirements or missing checks before review | That a PR with rework was bad work. #13 got a follow-up because the review found a real gap, which is the review doing its job |
| 4 | DoD checklist compliance | Ticked DoD boxes / total, over merged PRs | The scenario had defects reach production because checks were skipped | That ticked items were done well. A box can be ticked wrongly. It's only as honest as whoever ticks it |
| 5 | Blocked items | Open issues with the `blocked` label | Blocked work hides in "In Progress". This makes it visible so someone acts on it | Why it's blocked, or that whoever owns it did something wrong. Most blockers come from outside the item |
| 6 | Max PRs open at once (WIP in review) | Most PRs open at the same moment | Checks the WIP limit and the review-first experiment | That fewer is always better. With a real team, 2 or 3 open PRs can be normal |

Extra for the experiment: `ci_on_first_commit` counts PRs whose first commit got a CI check run.

## Reading the numbers carefully
- Sample size is tiny (a handful of PRs in one day), so medians move a lot with one PR.
- Times are in minutes because this was a compressed one-day cycle done by one person. They aren't comparable to a real team's days.
- If a metric looks off for one person, the first question is about the process (was the item clear, was it blocked, was review available), not about the person.
