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

    def get(self, appointment_id):
        return self._appointments[appointment_id]

    def all(self):
        return list(self._appointments.values())
