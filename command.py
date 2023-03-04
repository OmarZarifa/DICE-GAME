
from cmd import Cmd
from highScore import HighScore
from game import Game, Player


class Command(Cmd):
    intro = 'Type help or ? to list commands.\n'
    prompt = '> '

    def __init__(self):
        """Init game object."""
        super().__init__()
        self.game = None
        self.high_score = HighScore()

    def do_help(self, _):
        """Display the available commands"""
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
        """Display the rules of the game"""
        print("""
        Pig Dice is a game for two players, in which the players take turns rolling a single die.
        The goal of the game is to reach 100 points before the other player does.
        
        On each turn, the player rolls the die as many times as they want, accumulating points for each roll.
        However, if the player rolls a 1, they lose all the points they have accumulated on that turn, and the turn ends.
        If the player rolls a 6, they lose all the points they have accumulated in the game so far, and the turn ends.
        
        The player can choose to end their turn at any time and add their accumulated points to their total score.
        The turn then passes to the other player.
        
        If a player reaches 100 points, the game ends and that player wins.
        """)

    def do_start(self, arg):
        """Start a new game"""

        num_players = int(arg)
        if num_players == 1:
            player1_name = input("Please enter your name: ")
            level = input("Select computer intelligence level (dumb, medium or hard): ")
            self.game =  Game(player1_name, "computer")
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
        """Roll the dice"""
        if self.game is None:
            print("No game in progress. Use the 'start' command to start a new game.")
        elif self.game.is_game_over(self.game.current_player.score):
            self.do_restart(self)
        else:
            self.game.roll_dice()
            


    def do_pass(self, _):
        """Pass rolling to the other player"""
        if self.game is None:
            print("No game in progress. Use the 'start' command to start a new game.")
        else:
            self.game.pass_dice()
            self.do_roll(self)
            
            
            
    def do_restart(self, arg):
        """Restart the current game"""
        if self.game is None:
            print("No game in progress. Use the 'start' command to start a new game.")
        else:
            self.game.reset_game()
            print ("New game restarted")   
    
    
    def do_exit(self, _):
        """Exit the game"""
        print("Thank you for playing Pig Dice Game!")
        return True        


    def do_cheat(self, _):
        if self.game is None:
            print("No game in progress. Use the 'start' command to start a new game.")
        else:
            self.game.cheat()
            print(f"{self.game.current_player}, congrats, you win, cheater! ")
    
    def do_score(self, _):
        if self.game is None:
            print("No games are played. Use the 'start' command to start a new game.")
            
        else:
            self.game.highscore.display()
            
            
                             
    """
    def do_start(self, arg):
        #Start a new game
        if self.game is not None and not self.game.is_over:
            confirm = input("Are you sure you want to start a new game? (Y/N) ")
            if confirm.lower() != 'y':
                return
        try:
            num_players = int(arg)
            if num_players == 1:
                #player1_name = input("Enter your name: ")
                #level = input("Enter computer intelligence level (dumb, medium or hard): ")
                #self.game = Game(Player(player1_name), Player("Computer", level=int(level)))
                name = input("Please enter your name: ")
                level = input("Select computer intelligence level (dumb, medium or hard): ")
                game =  Game(name, "computer")
                game.computer_playing(level)
                
            elif num_players == 2:
                #player1_name = input("Enter player 1 name: ")
                #player2_name = input("Enter player 2 name: ")
                #self.game = Game(Player(player1_name), Player(player2_name))
                name1 = input("Enter the name of the first player: ")
                name2 = input("Enter the name of the second player: ")
                game = Game(name1, name2)
                game.human_playing()
                
            else:
                raise ValueError
            print("New game started.")
            self.game.show_scores()
        except ValueError:
            print("Invalid number of players. Please enter 1 or 2.")
    """

    def do_scores(self, arg):
        print(self.highscore)
        
    def do_high_score(self, arg):
        """Print the high score table"""
        print(self.highscore.get_high_score_table())

    def do_EOF(self, arg):
        """Terminate the shell"""
        return True

    def emptyline(self):
        """Override the method to do nothing, since we don't want the shell to repeat the last command if the user enters an empty line."""
        pass

    def default(self, line):
            print("Invalid command. Type 'help' or '?' to see list of available commands.")