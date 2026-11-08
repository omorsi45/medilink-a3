from dataclasses import dataclass
from datetime import datetime


@dataclass
class Appointment:
    id: int
    patient: str
    clinic: str
    start: datetime
    status: str = "booked"


class AppointmentBook:
    def __init__(self, reminders=None):
        self._appointments = {}
        self._next_id = 1
        self.reminders = reminders

    def book(self, patient, clinic, start):
        if self._slot_taken(clinic, start):
            raise ValueError(f"{clinic} already has a booking at {start}")
        appt = Appointment(self._next_id, patient, clinic, start)
        self._appointments[appt.id] = appt
        self._next_id += 1
        if self.reminders is not None:
            self.reminders.schedule(appt)
        return appt

    def cancel(self, appointment_id):
        appt = self._appointments.get(appointment_id)
        if appt is None:
            raise KeyError(f"no appointment {appointment_id}")
        appt.status = "cancelled"
        return appt

    def _slot_taken(self, clinic, start):
        return any(a.clinic == clinic and a.start == start
                   and a.status == "booked"
                   for a in self._appointments.values())

    def get(self, appointment_id):
        return self._appointments[appointment_id]

    def all(self):
        return list(self._appointments.values())
