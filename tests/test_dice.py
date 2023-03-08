import unittest
from unittest.mock import patch
import io
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
    def test_roll_face(self):
        dice = Dice()
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            dice.roll()
            rolled_face = dice.face
            if rolled_face == 1:
                expected_output = "+-------+\n|       |\n|   O   |\n|       |\n+-------+\n"
                self.assertEqual(fake_out.getvalue(), expected_output)
            elif rolled_face == 2:
                expected_output = "+-------+\n| O     |\n|       |\n|     O |\n+-------+\n"
                self.assertEqual(fake_out.getvalue(), expected_output)
            elif rolled_face == 3:
                expected_output = "+-------+\n| O     |\n|   O   |\n|     O |\n+-------+\n"
                self.assertEqual(fake_out.getvalue(), expected_output)
            elif rolled_face == 4:
                expected_output = "+-------+\n| O   O |\n|       |\n| O   O |\n+-------+\n"
                self.assertEqual(fake_out.getvalue(), expected_output)
            elif rolled_face == 5:
                expected_output = "+-------+\n| O   O |\n|   O   |\n| O   O |\n+-------+\n"
                self.assertEqual(fake_out.getvalue(), expected_output)
            elif rolled_face == 6:
                expected_output = "+-------+\n| O   O |\n| O   O |\n| O   O |\n+-------+\n"
                self.assertEqual(fake_out.getvalue(), expected_output)
            else:
                expected_output = "+-------+\n|       |\n|       |\n|       |\n+-------+\n"
                self.assertEqual(fake_out.getvalue(), expected_output)
    
        
    def test_get_face(self):
        dice = Dice()
        self.assertIn(dice.get_face(), range(1, 7))
        self.assertTrue(dice.get_face() <= 6)
        self.assertFalse(dice.get_face() > 6)


if __name__ == '__main__':
    unittest.main()
