
"""A class that represents a game of Pig."""

from app.intelligence import Intelligence
from app.dice import Dice
from app.player import Player
from app.highScore import HighScore


class Game:
    """
    A class that represents a game of Pig.

    Attributes:
        WINNING_SCORE (int): The score needed to win the game.
        p1 (Player): The first player.
        p2 (Player): The second player.
        current_player (Player): The current player.
        other_player (Player): The other player.
        winner (Player): The winner of the game.
        turn_score (int): The score for the current turn.
        dice_value (int): The value of the dice roll.
        level (str): The difficulty level of the game.
        highscore (HighScore): The high score list.
    """
    WINNING_SCORE = 50

    def __init__(self, player1_name, player2_name):
        self.p1 = Player(player1_name)
        self.p2 = Player(player2_name)
        self.current_player = self.p1
        self.other_player = self.p2
        self.winner = None
        self.turn_score = 0
        self.dice_value = None
        self.level = ""
        self.highscore = HighScore()

    def switch_players(self):
        """Switches the current player and the other player."""
        self.current_player, self.other_player = self.other_player, self.current_player

    def roll_dice(self):
        """Rolls the dice and updates the turn score."""
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
        """
        Rolls the dice for the computer player.

        Args:
            level (str): The difficulty level of the game.

        Returns:
            None
        """
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
        """Checks if the current player is a computer player."""
        if self.current_player.name == "computer":
            return True
        else:
            return False

    def pass_dice(self):
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
        '''Determines whether the game is over.'''
        '''Returns True if player has 100 or more, otherwise it returns False.'''
        if (current_player_score >= self.WINNING_SCORE):
            return True
        else:
            return False

    def reset_game(self):
        self.p1.score = 0
        self.p2.score = 0
        self.current_player = self.p1
        self.other_player = self.p2
        self.winner = None
        self.turn_score = 0
        self.dice_value = None

    def cheat(self):
        self.current_player.score += self.WINNING_SCORE
        self.winner = self.current_player
        self.highscore.add_score(self.current_player.score)
        self.highscore.add_name(self.winner.name)

    def set_current_player(self, name):
        self.current_player = name

    def set_other_player(self, name):
        self.other_player = name

    def get_current_player(self):
        return self.current_player

    def get_other_player(self):
        return self.other_player

    def set_level(self, level):
        self.level = level

    def get_level(self):
        return self.level
