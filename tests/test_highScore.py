
import unittest
from app.highScore import HighScore

class TestHighScore(unittest.TestCase):

    def setUp(self):
        self.highScore = HighScore()

    def test_add_score(self):
        # Ensure score is added to list of scores
        self.highScore.add_score(10)
        self.assertEqual(self.highScore.players_score, [10])

    def test_add_name(self):
        # Ensure name is added to list of names
        self.highScore.add_name("John")
        self.assertEqual(self.highScore.players_name, ["John"])

if __name__ == '__main__':
    unittest.main()
