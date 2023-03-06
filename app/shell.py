"""
The Shell module provides a simple shell interface for interacting with the command line.

The Shell class can be used to create a command line interface that accepts user input,
executes shell commands, and displays the output to the user.

Commands:
    The Shell supports the following commands:
        - help        - Display this help message")
        - rules       - Display the rules of the game")
        - start [1|2] - Start a new game against the computer or with two players")
        - roll        - Roll the dice")
        - pass        - Pass rolling to the other player")
        - restart     - Restart the current game")
        - exit        - Exit the current game")
        - cheat       - Cheat and reach 100 points in the game")
        - score       - Display the high scores")
"""


from cmd import Cmd
from app.highscore import HighScore
from app.game import Game


class Shell(Cmd):
    """Class Shell."""

    intro = 'Type help or ? to list commands.\n'
    prompt = '> '

    def __init__(self):
        """Initialize a new instance of the Shell class.

        Create a Game object and a HighScore object.
        """
        super().__init__()
        self.game = None
        self.high_score = HighScore()

    def do_help(self, _):
        """Display the available commands."""
        print("Available commands:")
        print("help        - Display this help message")
        print("rules       - Display the rules of the game")
        print("start [1|2] - Start a new game against the computer or with two players")
        print("roll        - Roll the dice")
        print("pass        - Pass rolling to the other player")
        print("restart     - Restart the current game")
        print("exit        - Exit the current game")
        print("cheat       - Cheat and reach 100 points in the game")
        print("score   - Display the high scores")

    def do_rules(self, _):
        """Display the rules of the game."""
        print("""
        Pig Dice is a game for two players, in which the players take turns rolling a single die.
        The goal of the game is to reach 100 points before the other player does.

        On each turn, the player rolls the die as many times as they want, accumulating points for each roll.
        However, if the player rolls a 1, they lose all the points they have accumulated on that turn, and the turn ends.
        If the player rolls a 6, they lose all the points they have accumulated in the game so far, and the turn ends.

        The player can choose to end their turn at any time and add their accumulated points to their total score.
        The turn then passes to the other player.

        If a player reaches 50 points, the game ends and that player wins.
        """)

    def do_start(self, arg):
        """Start a new game with one or two players, depending on the user's input."""
        num_players = int(arg)
        if num_players == 1:
            player1_name = input("Please enter your name: ")
            level = input("Select computer intelligence level (dumb, medium or hard): ")
            self.game = Game(player1_name, "computer")
            self.game.set_level(level)
            print("New game started.")

        elif num_players == 2:
            player1_name = input("Enter the name of the first player: ")
            player2_name = input("Enter the name of the second player: ")
            self.game = Game(player1_name, player2_name)
            print("New game started.")

        else:
            print("We were not able to start the game, please enter a valid choice using")
            print("'start 1' for playing with computer")
            print("'start 2' for playing with another player")

    def do_roll(self, _):
        """Roll the dice for the current player."""
        if self.game is None:
            print("No game in progress. Use the 'start' command to start a new game.")
        elif self.game.is_game_over(self.game.current_player.score):
            self.do_restart(self)
        else:
            self.game.roll_dice()

    def do_pass(self, _):
        """Pass rolling to the other player and do the first roll."""
        if self.game is None:
            print("No game in progress. Use the 'start' command to start a new game.")
        else:
            self.game.pass_dice()
            self.do_roll(self)

    def do_restart(self, _):
        """Restart the current game."""
        if self.game is None:
            print("No game in progress.Use the 'start 1' or 'start 2' command to start a new game.")
        else:
            self.game.reset_game()
            print("New game restarted")

    def do_exit(self, _):
        """Exit the game."""
        print("Thank you for playing Pig Dice Game!")
        return True

    def do_cheat(self, _):
        """Allow the current player to cheat and reach 50 points in the game."""
        if self.game is None:
            print("No game in progress. Use the 'start' command to start a new game.")
        else:
            self.game.cheat()
            print(f"{self.game.current_player}, congrats, you win, cheater! ")

    def do_score(self, _):
        """Display the high scores of all completed games."""
        if self.game is None:
            print("No games are played. Use the 'start' command to start a new game.")

        else:
            self.game.highscore.display()

    def do_eof(self, _):
        """Terminate the shell."""
        return True

    def emptyline(self):
        """Override the method to do nothing.

        since we don't want the shell to repeat the last command if the user enters an empty line.
        """

    def default(self, line):
        """Display an error message when the user enters an invalid command."""
        print("Invalid command. Type 'help' or '?' to see list of available commands.")
