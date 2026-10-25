import unittest
from app import check_threat_severity


class TestThreatSeverity(unittest.TestCase):

    def test_critical_threat(self):
        self.assertEqual(check_threat_severity(90), "Critical")

    def test_high_threat(self):
        self.assertEqual(check_threat_severity(60), "High")

    def test_low_threat(self):
        self.assertEqual(check_threat_severity(20), "Low")


if __name__ == "__main__":
    unittest.main()
