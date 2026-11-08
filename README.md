# MediLink A3

Small MediLink appointment and reminder module I use for COMP 354 Assignment 3 (Software Engineering Management in Practice). The code is small on purpose. The point of the repo is the workflow around it: issues, labels, PRs, the Definition of Done, the incident write-up and the metrics.

Individual submission: Omar Morsi (40236376).

## What the code does
- `medilink/appointments.py`: book, cancel and look up appointments.
- `medilink/reminders.py`: schedules a reminder 24 hours before each appointment and sends the ones that are due.

Python 3 standard library only.

## Run the tests
```
python3 -m unittest discover -v
```

## Docs
- [Workflow and WIP limit](docs/workflow.md)
- [Definition of Done](docs/definition-of-done.md)
- [Development plan](docs/development-plan.md)
- [SMART objective](docs/smart-objectives.md)
- [Communication](docs/communication.md)
- [Risk register](docs/risk-register.md)
- [Dashboard](docs/dashboard.md)
- [Incident RCA (Five Whys)](docs/rca-five-whys.md)
- [Coaching reflection](docs/coaching-session.md)
- [Improvement experiment](docs/experiment.md)
