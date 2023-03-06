"""A class representing the artificial intelligence (AI) of a game player."""


class Intelligence:
    """Class Intelligence."""

    def __init__(self, level):
        """Initialize a new Intelligence instance with the given difficulty level."""
        self.level = level

    def decide(self, round_score, total_score):
        """Return the AI's decision for the current round based on its level."""
        if self.level == "dumb":
            return self.dumb_level()

        if self.level == "medium":
            return self.medium_level(round_score)

        if self.level == "hard":
            return self.hard_level(round_score, total_score)

        # If none of the above conditions are met, return None
        return None

    def dumb_level(self):
        """Return "roll" as the decision for a dumb AI."""
        return "roll"

    def medium_level(self, round_score):
        """Return "roll" if the round score is less than 25, otherwise "pass"."""
        if round_score < 25:
            return "roll"
        return "pass"

    def hard_level(self, round_score, total_score):
        """Return "roll" or "pass" based on the round and total scores for a hard AI."""
        if round_score <= 10 and total_score < 30:
            return 'roll'
        if round_score < 8 and total_score >= 30:
            return 'roll'
        return 'pass'
