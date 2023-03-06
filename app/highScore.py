
"""
The HighScore class is for keeping track of high scores for a game.
The class stores player names and scores and can display a high score table.    
"""

class HighScore:
    """HighScore class"""

    def __init__(self):
        """
        Initializes an empty list for player names and an empty list for player scores.
        """
        self.players_name = []
        self.players_score = []

    def add_score(self, score):
        """Adds a player's score to the list of scores."""
        self.players_score.append(score)

    def add_name(self, name):
        """Adds a player's name to the list of names."""
        self.players_name.append(name)

    def display(self):
        """Displays the high score table with player names and scores."""
        # Print the table headers
        player = "Player"
        score = "Score"
        print(f"{player:<10} {score:<10}")
        print("=" * 20)
        # Print the table rows
        for i, name in enumerate(self.players_name):
            score = self.players_score[i]
            print(f"{name:<10} {score:<10}")
