import unittest
from app.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("player1", "player2")

    def test_switch_players(self):
        self.assertEqual(self.game.current_player, self.game.p1)
        self.assertEqual(self.game.other_player, self.game.p2)
        self.game.switch_players()
        self.assertEqual(self.game.current_player, self.game.p2)
        self.assertEqual(self.game.other_player, self.game.p1)

    def test_roll_dice(self):
        self.game.current_player = self.game.p1
        self.game.roll_dice()
        self.assertGreaterEqual(self.game.turn_score, 0)
        self.assertLessEqual(self.game.turn_score, 6)

    def test_computer_roll(self):
        self.game.current_player = self.game.p2
        self.game.set_level("hard")
        self.game.computer_roll(self.game.level)
        self.assertGreaterEqual(self.game.turn_score, 0)
        self.assertLessEqual(self.game.turn_score, 6)

    def test_is_computer(self):
        self.game = Game("player1", "computer")
        self.game.current_player = self.game.p1
        self.assertFalse(self.game.is_computer())
        self.game.current_player = self.game.p2
        self.assertTrue(self.game.is_computer())

    def test_pass_dice(self):
        self.game.current_player = self.game.p1
        self.game.turn_score = 20
        self.game.pass_dice()
        self.assertEqual(self.game.current_player, self.game.p2)
        self.assertEqual(self.game.turn_score, 0)
        self.assertEqual(self.game.p1.score, 20)

    def test_is_game_over(self):
        self.game.current_player = self.game.p1
        self.assertFalse(self.game.is_game_over(self.game.current_player.score))
        self.game.current_player.score = 50
        self.assertTrue(self.game.is_game_over(self.game.current_player.score))

    def test_reset_game(self):
        self.game.current_player = self.game.p2
        self.game.p1.score = 50
        self.game.reset_game()
        self.assertEqual(self.game.p1.score, 0)
        self.assertEqual(self.game.p2.score, 0)
        self.assertEqual(self.game.current_player, self.game.p1)
        self.assertIsNone(self.game.winner)
        self.assertEqual(self.game.turn_score, 0)
        self.assertIsNone(self.game.dice_value)

    def test_cheat(self):
        self.game.current_player = self.game.p1
        self.game.cheat()
        self.assertEqual(self.game.current_player.score, 50)
        self.assertEqual(self.game.winner, self.game.current_player)

    def test_set_current_player(self):
        self.game.set_current_player(self.game.p2)
        self.assertEqual(self.game.current_player, self.game.p2)

    def test_set_other_player(self):
        self.game.set_other_player(self.game.p1)
        self.assertEqual(self.game.other_player, self.game.p1)

    def test_get_current_player(self):
        self.assertEqual(self.game.get_current_player(), self.game.p1)

    def test_get_other_player(self):
        self.assertEqual(self.game.get_other_player(), self.game.p2)

    def test_set_level(self):
        self.game.set_level("easy")
        self.assertEqual(self.game.level, "easy")

    def test_get_level(self):
        self.game.set_level("hard")
        self.assertEqual(self.game.get_level(), "hard")


if __name__ == '__main__':
    unittest.main()
