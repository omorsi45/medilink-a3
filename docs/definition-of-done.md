# Definition of Done

An item only moves to Done when all of these are true. The same list is in the PR template so it gets ticked on every PR.

1. The acceptance criteria in the issue are met, and each one is checked off in the PR.
2. There's a unit test for the new behaviour. For a defect, there's a test that failed before the fix and passes after.
3. `python3 -m unittest discover` passes locally and the CI check is green.
4. The PR links its issue (`Closes #N` or `Refs #N`).
5. The PR got a review pass with written comments before merge (see note below).
6. README or docs are updated if behaviour or setup changed.
7. Verification: I ran the scenario from the issue one more time on `main` after merge and wrote the result as a comment on the issue.

Note on review: I'm doing this assignment alone, so the review is a self-review done as a separate step after the PR is opened, using this checklist. That isn't the same as a second person reviewing, and I count it that way in the dashboard.
