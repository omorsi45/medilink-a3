# Workflow

Backlog → Ready → In Progress → Code Review → Verification → Done

GitHub labels stand for each state (`status:backlog`, `status:ready`, `status:in-progress`, `status:code-review`, `status:verification`, `status:done`). The project board uses the same six columns.

| State | Means | Enter when |
|---|---|---|
| Backlog | Idea or request, not ready yet | Issue created |
| Ready | Can be started | Has acceptance criteria, priority, owner, and nothing blocking it |
| In Progress | Someone is working on it | A branch exists for it |
| Code Review | PR is open | PR opened with the DoD checklist |
| Verification | Merged, checking on `main` | PR merged, scenario not re-run yet |
| Done | Finished | DoD item 7 written on the issue |

A `blocked` label goes on top of the state when something outside the item stops it. The blocker gets written in a comment.

## WIP limit

WIP limit: 2 items total across In Progress + Code Review.

Why 2: I'm one person doing this cycle. The handout scenario says developers kept starting new work while old work sat waiting for review. With a limit of 1, I'd have nothing to do while CI runs or while I wait on an answer. With 3 or more, I'd just repeat the scenario's problem. 2 lets one item wait in review while I work on one other thing, and no more. If I'm at 2, the next move is finishing a review, not starting something new.

Review-first rule (from the experiment in docs/experiment.md, decision: Modify): at most one of your own PRs waiting at a time. If you have one waiting, your next task is a review, not a new item.

The limit doesn't count Verification, since that step is short and doesn't block new work.

## Incident rule
Any P1 incident gets a short Five Whys RCA in `docs/` before its issue is closed. Added after incident #1 (see docs/rca-five-whys.md).
