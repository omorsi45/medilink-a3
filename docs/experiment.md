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
From `data/metrics_output.txt` (export at 5:27 PM ET, Nov 8):

| Measure | Before (#11, #12, #13) | After (#14, #15, #16) | Target met? |
|---|---|---|---|
| Max PRs open at once | 3 | 1 | Yes |
| PRs with a CI check on the first commit | 1/3 | 3/3 | Yes, but see below |
| Median minutes, opened to first review | 3.1 | 0.6 | Yes (not worse) |
| Median minutes, opened to merge | 3.3 | 0.9 | n/a |
| First-Time-Right | 2/3 | 3/3 | n/a |
| DoD checklist ticked | 18/18 | 16/18 | n/a, went down |

What the numbers do and don't say:
- Max open PRs went from 3 to 1. That one really is the rule, because the rule is literally "don't open a second PR".
- CI on first commit going from 1/3 to 3/3 is mostly not the rule. #12 and #13 had no CI because #11 hadn't merged yet. Every "after" branch was made after CI was on main. The rule would have prevented it (review #11 first, then branch), but I can't separate the two here.
- Review times are in minutes because the whole cycle took about 15 minutes of PR activity. One PR can move the median a lot.
- DoD compliance went down. That's two honest misses (#14 no failing-test-first, #16 no linked issue), not the rule making things worse. The checklist did its job by showing them.
- 3 PRs vs 3 PRs, one person, one day. This can't prove the rule caused anything.

Feedback (mine, since I'm the only one on the team): working one PR at a time felt simpler. I never had to merge main back into a branch after the rule started, and before it I had to do it twice. The cost showed up on #15: I waited for CI to finish before reviewing, which is most of its 1.1 minutes. On a real team, waiting on a reviewer would take much longer than CI, so "do nothing until it's merged" wouldn't scale.

## Decision
**Modify.**

The part that clearly worked (at most one PR waiting per person, review before starting new work) stays, and goes into docs/workflow.md as part of the WIP policy. What changes for a team: instead of "merge before starting anything", the rule becomes "if you have a PR waiting, your next task is a review of someone else's PR, not a new item". That keeps WIP low without everyone sitting idle waiting for a reviewer. I'd re-run the same measurements with Group 14 over a real multi-day cycle, with more PRs, before deciding to fully adopt.
