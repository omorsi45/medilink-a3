from dataclasses import dataclass
from datetime import datetime, timedelta

DEFAULT_LEAD = timedelta(hours=24)


@dataclass
class Reminder:
    appointment_id: int
    patient: str
    send_at: datetime


class ReminderScheduler:
    def __init__(self, lead=DEFAULT_LEAD, is_active=None):
        self.lead = lead
        # is_active(appointment_id) -> bool. Second guard for incident #1:
        # never send a reminder for an appointment that isn't booked anymore.
        self.is_active = is_active
        self._pending = []
        self.sent = []

    def schedule(self, appointment):
        reminder = Reminder(appointment.id, appointment.patient,
                            appointment.start - self.lead)
        self._pending.append(reminder)
        return reminder

    def cancel(self, appointment_id):
        """Drop every pending reminder for this appointment."""
        self._pending = [r for r in self._pending
                         if r.appointment_id != appointment_id]

    def pending(self):
        return list(self._pending)

    def send_due(self, now):
        """Send every reminder whose time has come. Returns what was sent."""
        due = [r for r in self._pending if r.send_at <= now]
        sent = []
        for r in due:
            self._pending.remove(r)
            if self.is_active is not None and not self.is_active(r.appointment_id):
                continue
            self.sent.append(r)
            sent.append(r)
        return sent
