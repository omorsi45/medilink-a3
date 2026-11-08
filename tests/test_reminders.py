import unittest
from datetime import datetime, timedelta

from medilink.appointments import AppointmentBook
from medilink.reminders import ReminderScheduler


class ReminderTests(unittest.TestCase):
    def setUp(self):
        self.reminders = ReminderScheduler()
        self.book = AppointmentBook(self.reminders)
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


if __name__ == "__main__":
    unittest.main()
