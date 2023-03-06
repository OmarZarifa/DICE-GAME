
"""Here the pig dice game is taking place"""

from app.intelligence import Intelligence
from app.dice import Dice
from app.player import Player
from app.highscore import HighScore


class Game:
    """Class Game"""
    WINNING_SCORE = 50

    def __init__(self, player1_name, player2_name):
        self.player_1 = Player(player1_name)
        self.player_2 = Player(player2_name)
        self.current_player = self.player_1
        self.other_player = self.player_2
        self.winner = None
        self.turn_score = 0
        self.dice_value = None
        self.level = ""
        self.highscore = HighScore()
        self.value = None
        self.value1 = None
        self.dice_value1 = None

    def switch_players(self):
        """Switche the current player and the other player."""
        self.current_player, self.other_player = self.other_player, self.current_player

    def roll_dice(self):
        """Roll the dice and updates the turn score."""
        if self.is_computer():
            self.computer_roll(self.level)

        else:
            self.value = Dice()
            self.dice_value = self.value.roll()
            if self.dice_value == 1:
                self.turn_score = 0
                print(f"{self.current_player}, your turn score is {self.turn_score}.\n")
                self.switch_players()
                self.roll_dice()
            else:
                self.turn_score += self.dice_value
                print(f"{self.current_player}, your turn score is {self.turn_score}.\n")

    def computer_roll(self, level):
        """Roll the dice for the computer player."""
        intelligence = Intelligence(level)

        self.turn_score = 0
        again = 'y'
        # establish a while loop for the computer's turn
        while again == 'y':
            self.value1 = Dice()
            self.dice_value1 = self.value1.roll()

            if self.dice_value1 == 1:
                self.turn_score = 0
                print(f"{self.current_player}, your turn score is {self.turn_score}.\n")
                self.switch_players()
                self.roll_dice()
                again = 'n'

            else:
                self.turn_score += self.dice_value1
                print(f"{self.current_player}, your turn score is {self.turn_score}.\n")
                roll_or_hold = intelligence.decide(self.turn_score, self.current_player.score)
                if roll_or_hold == 'roll':
                    again = 'y'
                else:
                    again = 'n'
                    self.pass_dice()

    def is_computer(self):
        """Check if the current player is a computer player."""
        return bool(self.current_player.name == "computer")

    def pass_dice(self):
        """
        Pass the turn to the other player and
        add the current turn score to the current player's total score.

        If the current player's total score reaches the winning score
        set the winner and update the high score list.
        """
        self.current_player.add_score(self.turn_score)
        self.turn_score = 0
        if self.current_player.score >= self.WINNING_SCORE:
            self.winner = self.current_player
            self.highscore.add_score(self.current_player.score)
            self.highscore.add_name(self.winner.name)
            print(f"Congrats {self.current_player.name}, you are the winner! \n")
        else:
            self.switch_players()

    def is_game_over(self, current_player_score):
        """Determine whether the game is over.
        Return True if player has 50 or more, otherwise return False.
        """
        return bool(current_player_score >= self.WINNING_SCORE)

    def reset_game(self):
        """Reset the game by resetting all the attributes to their default values:"""
        self.player_1.score = 0
        self.player_2.score = 0
        self.current_player = self.player_1
        self.other_player = self.player_2
        self.winner = None
        self.turn_score = 0
        self.dice_value = None

    def cheat(self):
        """Set the score of the current player to WINNING_SCORE (50)"""
        self.current_player.score += self.WINNING_SCORE

        # declare the current player as the winner
        self.winner = self.current_player

        # add the current player's score and name to the high score table
        self.highscore.add_score(self.current_player.score)
        self.highscore.add_name(self.winner.name)

    def set_current_player(self, name):
        """Set the current player to the player with the given name."""
        self.current_player = name

    def set_other_player(self, name):
        """Set the other player to the player with the given name."""
        self.other_player = name

    def get_current_player(self):
        """Return the current player."""
        return self.current_player

    def get_other_player(self):
        """Return the other player."""
        return self.other_player

    def set_level(self, level):
        """Set the game level to the given level."""
        self.level = level

    def get_level(self):
        """Return the current game level."""
        return self.level
