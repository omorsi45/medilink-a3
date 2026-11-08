import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import metrics  # noqa: E402


def pr(n, created, merged, reviews, commits, body="- [x] a\n- [ ] b"):
    return {"number": n, "createdAt": created, "mergedAt": merged, "closedAt": merged,
            "reviews": [{"submittedAt": r} for r in reviews],
            "commits": [{"committedDate": c} for c in commits], "body": body}


class MetricsTests(unittest.TestCase):
    def test_turnaround_and_lead_time(self):
        p = pr(1, "2026-11-08T10:00:00Z", "2026-11-08T10:30:00Z",
               ["2026-11-08T10:10:00Z"], ["2026-11-08T09:50:00Z"])
        self.assertEqual(metrics.review_turnaround(p), 10.0)
        self.assertEqual(metrics.lead_time(p), 30.0)

    def test_first_time_right(self):
        clean = pr(1, "2026-11-08T10:00:00Z", None, ["2026-11-08T10:10:00Z"],
                   ["2026-11-08T09:50:00Z"])
        rework = pr(2, "2026-11-08T10:00:00Z", None, ["2026-11-08T10:10:00Z"],
                    ["2026-11-08T09:50:00Z", "2026-11-08T10:20:00Z"])
        self.assertTrue(metrics.first_time_right(clean))
        self.assertFalse(metrics.first_time_right(rework))

    def test_no_review_gives_none(self):
        p = pr(1, "2026-11-08T10:00:00Z", None, [], ["2026-11-08T09:50:00Z"])
        self.assertIsNone(metrics.review_turnaround(p))
        self.assertIsNone(metrics.first_time_right(p))

    def test_checklist(self):
        p = pr(1, "2026-11-08T10:00:00Z", None, [], [])
        self.assertEqual(metrics.checklist(p), (1, 2))

    def test_max_concurrent(self):
        a = pr(1, "2026-11-08T10:00:00Z", "2026-11-08T11:00:00Z", [], [])
        b = pr(2, "2026-11-08T10:30:00Z", "2026-11-08T12:00:00Z", [], [])
        c = pr(3, "2026-11-08T11:30:00Z", "2026-11-08T13:00:00Z", [], [])
        self.assertEqual(metrics.max_concurrent([a, b, c], "2026-11-08T14:00:00Z"), 2)


if __name__ == "__main__":
    unittest.main()
