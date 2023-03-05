import unittest
from app.intelligence import Intelligence


class TestIntelligence(unittest.TestCase):

    def setUp(self):
        self.dumb_intel = Intelligence("dumb")
        self.medium_intel = Intelligence("medium")
        self.hard_intel = Intelligence("hard")

    def test_dumb_level(self):
        self.assertEqual(self.dumb_intel.decide(0, 0), "roll")
        self.assertEqual(self.dumb_intel.decide(10, 50), "roll")

    def test_medium_level(self):
        self.assertEqual(self.medium_intel.decide(10, 0), "roll")
        self.assertEqual(self.medium_intel.decide(30, 0), "pass")

    def test_hard_level(self):
        self.assertEqual(self.hard_intel.decide(10, 20), "roll")
        self.assertEqual(self.hard_intel.decide(5, 40), "roll")
        self.assertEqual(self.hard_intel.decide(20, 40), "pass")


if __name__ == '__main__':
    unittest.main()
