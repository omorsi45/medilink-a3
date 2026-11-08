# SMART objective

The handout asks for one SMART objective per team member. I'm the only member, so I have one objective for the cycle.

**Objective:** By 11:59 PM ET on Sun Nov 8, 2026, get the two P1 items (#1, #2) to Done and the P2 items #3, #4 and #5 to at least Verification, with every merged PR ticking all 6 DoD checklist items and a green CI check.

| | |
|---|---|
| Specific | Five named issues, one clear end state each |
| Measurable | Issue states on the board, DoD checklist compliance and CI result from `scripts/metrics.py` |
| Achievable | Each item is small (one module, a few tests). Five items fits one long day for one person |
| Relevant | The P1s are the incident and the double-booking risk. CI and the checklist go after "defects reached production because verification was missed" |
| Time-bound | 11:59 PM ET, Nov 8, 2026 |

## Result (end of cycle, 5:30 PM ET)
- #1, #2, #3, #4, #5: all Done before the deadline. Met.
- CI green on every merged PR. Met.
- All 6 DoD items ticked on every merged PR: not met. #14 missed "failing test first" and #16 had no linked issue (34/36 boxes overall, from data/metrics_output.txt).

So the objective was partly met. The miss on #14 is what the coaching reflection (docs/coaching-session.md) is about.
