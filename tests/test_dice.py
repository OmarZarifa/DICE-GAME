import unittest
from unittest.mock import patch
from app.dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        """setUp method to create an instance of the Dice class before each test method is run"""
        self.dice = Dice()

    def test_roll(self):
        # Test with a random face value
        face = self.dice.roll()
        self.assertIn(face, range(1, 7))

        # Ensure roll returns an integer between 1 and 6 inclusive
        self.assertIsInstance(face, int)
        self.assertGreaterEqual(face, 1)
        self.assertLessEqual(face, 6)

if __name__ == '__main__':
    unittest.main()