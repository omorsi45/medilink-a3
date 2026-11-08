import unittest
from datetime import datetime

from medilink.appointments import AppointmentBook


class BookingTests(unittest.TestCase):
    def setUp(self):
        self.book = AppointmentBook()
        self.start = datetime(2026, 11, 20, 10, 0)

    def test_book_gives_new_id(self):
        a = self.book.book("Ana", "Clinic A", self.start)
        b = self.book.book("Ben", "Clinic A", datetime(2026, 11, 20, 11, 0))
        self.assertNotEqual(a.id, b.id)
        self.assertEqual(a.status, "booked")

    def test_cancel_sets_status(self):
        a = self.book.book("Ana", "Clinic A", self.start)
        self.book.cancel(a.id)
        self.assertEqual(self.book.get(a.id).status, "cancelled")

    def test_cancel_unknown_id(self):
        with self.assertRaises(KeyError):
            self.book.cancel(99)

    def test_double_booking_refused(self):
        self.book.book("Ana", "Clinic A", self.start)
        with self.assertRaises(ValueError):
            self.book.book("Ben", "Clinic A", self.start)

    def test_cancelled_slot_can_be_rebooked(self):
        a = self.book.book("Ana", "Clinic A", self.start)
        self.book.cancel(a.id)
        b = self.book.book("Ben", "Clinic A", self.start)
        self.assertEqual(b.status, "booked")

    def test_same_time_other_clinic_ok(self):
        self.book.book("Ana", "Clinic A", self.start)
        b = self.book.book("Ben", "Clinic B", self.start)
        self.assertEqual(b.clinic, "Clinic B")


if __name__ == "__main__":
    unittest.main()
