import unittest
from datetime import datetime, timedelta

from medilink.appointments import AppointmentBook
from medilink.reminders import ReminderScheduler

FIXED_NOW = datetime(2026, 11, 8, 9, 0)


class ReminderTests(unittest.TestCase):
    def setUp(self):
        self.reminders = ReminderScheduler()
        self.book = AppointmentBook(self.reminders, clock=lambda: FIXED_NOW)
        self.start = datetime(2026, 11, 20, 10, 0)

    def test_reminder_scheduled_24h_before(self):
        self.book.book("Ana", "Clinic A", self.start)
        [r] = self.reminders.pending()
        self.assertEqual(r.send_at, self.start - timedelta(hours=24))

    def test_send_due_only_sends_due(self):
        self.book.book("Ana", "Clinic A", self.start)
        sent = self.reminders.send_due(self.start - timedelta(hours=30))
        self.assertEqual(sent, [])
        sent = self.reminders.send_due(self.start - timedelta(hours=23))
        self.assertEqual(len(sent), 1)

    def test_cancelled_appointment_gets_no_reminder(self):
        # Incident #1: patients who cancelled still got the reminder
        cancelled = self.book.book("Ana", "Clinic A", self.start)
        kept = self.book.book("Ben", "Clinic A", datetime(2026, 11, 20, 11, 0))
        self.book.cancel(cancelled.id)
        sent = self.reminders.send_due(self.start)
        sent_ids = [r.appointment_id for r in sent]
        self.assertNotIn(cancelled.id, sent_ids)
        self.assertIn(kept.id, sent_ids)

    def test_cancel_removes_pending_reminder(self):
        a = self.book.book("Ana", "Clinic A", self.start)
        self.book.cancel(a.id)
        self.assertEqual(self.reminders.pending(), [])

    def test_send_due_skips_appointment_cancelled_another_way(self):
        # Second guard: even if status changes without cancel(), no reminder
        a = self.book.book("Ana", "Clinic A", self.start)
        self.book.get(a.id).status = "cancelled"
        sent = self.reminders.send_due(self.start)
        self.assertEqual(sent, [])


if __name__ == "__main__":
    unittest.main()
