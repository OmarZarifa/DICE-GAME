import unittest
from unittest.mock import patch
from io import StringIO
from app.dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        """setUp method to create an instance of the Dice class before each test method is run"""
        self.d = Dice()

    def test_roll(self):
        # Test with a mock output
        expected_output = "┌─────────┐\n│  ●   ●  │\n│  ●   ●  │\n│  ●   ●  │\n└─────────┘\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.d.roll()
            self.assertEqual(fake_output.getvalue(), expected_output)

        # Test with a random face value
        face = self.d.roll()
        self.assertIn(face, range(1, 7))

if __name__ == '__main__':
    unittest.main()

"""
In this example, we create a test class TestDice that subclasses unittest.TestCase. We define a setUp method to create an instance of the Dice class before each test method is run.

We then define one test method test_roll to test the roll method of the Dice class. In the first part of the test, we use the patch context manager from the unittest.mock module to mock the output of the print function. We then call the roll method and compare the output to the expected output for a dice face value of 6.

In the second part of the test, we call the roll method again without mocking the output, and assert that the returned face value is between 1 and 6.

Finally, we call unittest.main() to run the tests.
"""