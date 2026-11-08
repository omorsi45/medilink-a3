"""Re-run the issue scenarios for #1, #2 and #4 on main (DoD item 7)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from datetime import datetime
from medilink.appointments import AppointmentBook
from medilink.reminders import ReminderScheduler
r = ReminderScheduler(); b = AppointmentBook(r, clock=lambda: datetime(2026, 11, 8, 9, 0))
t = datetime(2026, 11, 20, 10, 0)
a = b.book("Ana", "Clinic A", t); k = b.book("Ben", "Clinic A", datetime(2026, 11, 20, 11, 0))
b.cancel(a.id)
print("#1 sent after cancel:", [x.appointment_id for x in r.send_due(t)], "(expected [2])")
try:
    b.book("Cam", "Clinic A", datetime(2026, 11, 20, 11, 0)); print("#2 double booking allowed (BAD)")
except ValueError as e:
    print("#2 double booking refused:", e)
c = b.book("Dan", "Clinic A", t); print("#2 rebook cancelled slot:", c.status)
try:
    b.book("Eve", "Clinic A", datetime(2026, 11, 1, 9, 0)); print("#4 past booking allowed (BAD)")
except ValueError as e:
    print("#4 past booking refused:", e)
