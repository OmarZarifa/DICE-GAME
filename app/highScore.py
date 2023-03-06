
"""
The HighScore class is for keeping track of high scores for a game.

The class stores player names and scores and can display a high score table.    
"""

class HighScore:
    """
    A class for keeping track of high scores for a game.
    """
    def __init__(self):
        """
        Initializes an empty list for player names and an empty list for player scores.
        """
        self.players_name = []
        self.players_score = []

    def add_score(self, score):
        """
        Adds a player's score to the list of scores.

        Args:
            score (int): The score to add to the list.
        """
        self.players_score.append(score)

    def add_name(self, name):
        """
        Adds a player's name to the list of names.

        Args:
            name (str): The name to add to the list.
        """
        self.players_name.append(name)

    def display(self):
        """
        Displays the high score table with player names and scores.
        """
        # Print the table headers
        print("{:<10} {:<10}".format("Player", "Score"))
        print("=" * 20)

        # Print the table rows
        for i in range(len(self.players_name)):
            print("{:<10} {:<10}".format(self.players_name[i], self.players_score[i]))
