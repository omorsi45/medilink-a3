# Improvement experiment: review before starting new work

Plan written at checkpoint 2, after PRs #11 to #13 and before #4 and #5 were started. The Result and Decision sections were filled in at the end of the cycle from `scripts/metrics.py`.

## Observed problem
In the first half of the cycle I did what the handout scenario describes: I opened a PR and then started the next item while the PR waited.
- #11 (CI) was still waiting when I opened #12 and #13. Because of that, #12 and #13 were branched without the CI workflow and got no check until I merged #11 and merged main back in. That cost an extra merge commit on each branch.
- When incident #1 came in, I had 3 items across In Progress + Code Review, over the WIP limit of 2.
- All three PRs were open at the same time.

## Proposed change
"Review first" rule for the rest of the cycle: after I open a PR, I do its review pass and merge it (or fix what the review finds) before I create the next branch. So at most one PR waits at a time. Incidents can still jump in, but they have to be written down on the issue like I did for #1.

## Expected result
- No more than 1 open PR at a time (before: 3).
- Every PR gets a CI check on its first push (before: 2 of 3 didn't).
- Time from opening a PR to its first review goes down, or at least doesn't go up.

## Measurement
`scripts/metrics.py` over the gh export (`data/github_export.json`), splitting PRs into before (#11, #12, #13) and after (the PRs for #4 and #5):
1. Max PRs open at the same time
2. PRs whose first commit got a CI check
3. Median minutes from PR opened to first review
4. Median minutes from PR opened to merge

Success: 1 and 2 hit their targets, and 3 is not worse than before.

Limits I know up front: it's 3 PRs vs 2 PRs, done by one person on one day, in minutes rather than days. That's way too small to prove anything. Also, because I wrote the rule myself, I can't separate "the rule helped" from "I was paying more attention". I'll use the numbers plus my own notes as feedback, and there's no team feedback to collect.

## Result
(Filled in at the end of the cycle.)

## Decision
(Filled in at the end of the cycle.)
