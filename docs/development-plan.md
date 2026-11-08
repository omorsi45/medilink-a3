# Development plan: Release 2.4 (compressed cycle)

I'm doing A3 as an individual submission (approved by the prof on Oct 28 at about a quarter to half of the team workload). So this is one short development cycle run by one person on Sun Nov 8, 2026, with three checkpoints that stand in for the "days" of the cycle.

## Roles
I hold every role, so I wrote down which hat I'm wearing for each kind of work:
- Engineering manager / team lead: keeps the backlog ready, enforces the WIP limit, runs the RCA, keeps the risk register and dashboard, runs the experiment.
- Developer: writes the code and tests, opens PRs.
- Reviewer: does the review pass on each PR as a separate step, using the DoD checklist.

The handout says the manager shouldn't just solve every technical problem. Alone, I can't split that between people, so what I did instead was keep the manager work (planning, RCA, metrics) in its own docs and comments, separate from the code.

## Scope and order
| Order | Issue | Why this order |
|---|---|---|
| 1 | #3 CI | Everything after it gets an automatic test check |
| 2 | #2 Double booking (P1) | Highest priority feature |
| 3 | #1 Incident: cancelled reminders (P1) | Reported during the cycle, jumps the queue |
| 4 | #4 Past bookings (P2) | Small defect |
| 5 | #5 Metrics script (P2) | Needed for the dashboard and experiment |
| 6 | #6 Admin day list (P2) | Start if time allows |
| later | #7, #8, #9 | Backlog for next cycle |

## Checkpoints
1. Start of cycle: plan, backlog ready, CI started.
2. Mid cycle: P1 items in review, incident handled.
3. End of cycle: metrics, experiment result, what's left.

## Dependencies
- #5 needs the PRs from #2, #1 and #4 to exist so there's real data to measure.
- #1's fix touches the same code as #2 (`AppointmentBook`), so they shouldn't both be half done for long.

## Done for the cycle
P1 items Done, P2 items #3 #4 #5 at least in Verification, and every merged PR passing the DoD checklist.
