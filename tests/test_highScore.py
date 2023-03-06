import unittest
import io
from app.highscore import HighScore
import unittest.mock 


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

    def test_display_with_score(self):
        # Ensure name and scores is added
        self.highScore.add_name("Alice")
        self.highScore.add_score(100)
        expected_output = "Player     Score     \n" \
                          "====================\n" \
                          "Alice      100"

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_output:
            self.highScore.display()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    def test_display_without_score(self):

        expected_output = "Player     Score     \n" \
                          "===================="

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_output:
            self.highScore.display()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
