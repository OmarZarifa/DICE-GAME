"""A class representing a player in a game."""


class Player:
    """Class Player."""

    def __init__(self, name):
        """Initialize a new Player instance with the given name."""
        self.name = name
        self.score = 0

    def add_score(self, score):
        """Increase the player's score by the given amount."""
        self.score += score

    def reset_score(self):
        """Reset the player's score to zero."""
        self.score = 0

    def set_name(self, new_name):
        """Set the player's name to the given value."""
        self.name = new_name
        print(f"Your new name is {new_name}, you can continue your playing by this name ")

    def __str__(self):
        """Return a string representation of the player (the player's name)."""
        return self.name
