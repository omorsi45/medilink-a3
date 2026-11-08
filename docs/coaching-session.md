# Coaching: structured self-coaching reflection

The handout asks for a coaching session between a manager and a developer. I'm doing this assignment alone, so I did it as a self-coaching reflection: I took a real difficulty from this cycle and went through it with coaching questions, answering them honestly, instead of jumping to the fix. It isn't the same as being coached by another person, and I don't present it that way.

## Problem / context
On PR #14 (defect #4, bookings in the past) I missed the DoD item "failing test first, then fix". I wrote the test and the fix in one commit. When I tried to show the test failing on the old code afterwards, the tests errored on the new `clock` argument instead of failing on the actual bug, so I couldn't show it.

The first defect (#1, the incident) did follow the rule: failing test, red CI, then the fix.

## Questions I worked through
1. What was different about #4 compared to #1, where failing-test-first worked?
2. What did the old code need before a test could even describe the bug?
3. At what point did I decide to put the change and the test together, and why did that feel OK then?
4. What would have told me earlier that I was skipping the step?
5. What's the smallest change to how I work that would make this hard to skip next time?

## What I learned
- In #1 the bug could be tested through the existing interface. In #4 it couldn't, because the code had no way to fix "now" in a test. So the test needed a small change to the code first.
- I bundled that change (adding `clock`) with the fix, which mixed "make it testable" with "fix it". That's why I couldn't show the test failing for the right reason.
- It felt OK because the change was small and CI was green. Green CI after the fact doesn't show the test would have caught the bug.
- Nothing warned me. The DoD box is only checked when I fill in the PR, which is after the commits are made.

## Agreed improvement action
For defects, split the work into up to three commits: (1) only the change needed to make the bug testable, with no behaviour change, (2) the failing test, pushed so CI goes red, (3) the fix.

## How to evaluate it later
In the next cycle, count defect PRs where the first CI run with the new test failed on an assertion (not an error). Target: every defect PR. The "Unit test added (defects: failing test first)" box on those PRs should be ticked and match what CI shows. I can add this to `scripts/metrics.py` by checking the CI result on the second commit of `type:defect` PRs.

## Collaborative vs directive decisions (for when I'm in Group 14)
I can't make team decisions alone, so this is what I'd do once I join Group 14 for A4.

- Collaborative: the WIP limit and the Definition of Done. Everyone works under them every day, and they only work if people actually agree with them. If I set them alone, people would work around them. The team should pick them together and review them after a cycle using the dashboard.
- Directive: during a P1 production incident like #1. Patients are getting wrong reminders right now, so there's no time to discuss. The manager should say directly who owns the fix, that their other work stops, and that the incident gets an RCA before it's closed. The team can discuss the process afterwards, in the RCA.
