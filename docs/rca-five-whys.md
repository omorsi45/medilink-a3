# Incident #1: Five Whys RCA

Incident: patients who cancel an appointment sometimes still get the reminder.
Issue: #1. Fix: PR #13.

The incident itself comes from the A3 handout scenario. The bug behind it was real in this repo: I reproduced it with a test, CI went red on PR #13 ([run](https://github.com/omorsi45/medilink-a3/actions/runs/42529469228)), and the fix turned it green. This RCA is about the process, not about who wrote the code.

## Chain
| Level | What |
|---|---|
| Symptom | A patient who cancelled gets the reminder 24h before the old appointment time |
| Immediate cause | `AppointmentBook.cancel()` only set `status = "cancelled"`. The reminder stayed in `ReminderScheduler`'s pending list, and `send_due()` sent everything due without looking at the appointment |
| Contributing factors | (1) Tests checked booking and reminders separately, never "cancel, then send reminders". (2) There was no CI before #3, so a test that did exist could still be skipped. (3) The cancel requirement only said what happens to the appointment, not what else depends on it. (4) In the scenario the team is interrupted by support requests, and the last incident was fixed fast with no follow-up, so nobody asked these questions before |
| Underlying causes | (1) Our process has no step that asks "what else reads this data?" when a state change is defined or reviewed. (2) There's no habit of investigating incidents, so the same kind of gap can come back |

## Five Whys
1. Why did the patient get a reminder after cancelling? Because the reminder was still in the pending list when `send_due()` ran.
2. Why was it still pending? Because cancelling only changed the appointment's status. Nothing told the reminder scheduler.
3. Why didn't `send_due()` notice the appointment was cancelled? Because the scheduler has its own copy of the reminder and never checks the appointment. Two parts share data with no rule about who updates what.
4. Why didn't a test catch it before production? Because the tests only covered each part alone, and nothing forced tests to run (no CI).
5. Why was there no test for cancel + reminder together? Because the acceptance criteria for cancelling didn't mention reminders at all. Nobody was asked to think about what else uses the appointment's status.

## Actions
| # | Type | Action | Where | Status |
|---|---|---|---|---|
| 1 | Corrective | `cancel()` removes the pending reminder | PR #13 | Done |
| 2 | Corrective | Second guard: `send_due()` skips any reminder whose appointment isn't booked (came out of the review on #13) | PR #13 | Done |
| 3 | Preventive | Regression test for cancel + reminder, run by CI on every PR | PR #13, PR #11 | Done |
| 4 | Preventive | Work item template asks "What else uses this data?" so acceptance criteria cover side effects | `.github/ISSUE_TEMPLATE/work-item.md`, this PR | Done |
| 5 | Preventive | Any P1 incident gets a short RCA before its issue is closed | docs/workflow.md, this PR | Done |

## How I'll know the actions worked
- Action 3: the test stays in the suite and CI stays green on later PRs.
- Action 4: new work items show a filled "What else uses this data?" section. I can count that in the next cycle.
- Action 1 and 2 can't be fully proven by one test. They lower the risk, they don't prove no other path sends a wrong reminder.
