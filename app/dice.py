
"""A class representing a standard six-sided dice."""

import random


class Dice:
    """Dice Class."""

    def __init__(self):
        """Initializes a new instance of the Dice class."""
        self.face = random.randint(1, 6)

    def roll(self):
        """Roll and print the rolled dice face."""
        self.face = random.randint(1, 6)
        if self.face == 1:
            print("+-------+")
            print("|       |")
            print("|   O   |")
            print("|       |")
            print("+-------+")

        elif self.face == 2:
            print("+-------+")
            print("| O     |")
            print("|       |")
            print("|     O |")
            print("+-------+")

        elif self.face == 3:
            print("+-------+")
            print("| O     |")
            print("|   O   |")
            print("|     O |")
            print("+-------+")

        elif self.face == 4:
            print("+-------+")
            print("| O   O |")
            print("|       |")
            print("| O   O |")
            print("+-------+")

        elif self.face == 5:
            print("+-------+")
            print("| O   O |")
            print("|   O   |")
            print("| O   O |")
            print("+-------+")

        elif self.face == 6:
            print("+-------+")
            print("| O   O |")
            print("| O   O |")
            print("| O   O |")
            print("+-------+")

        else:
            print("+-------+")
            print("|       |")
            print("|       |")
            print("|       |")
            print("+-------+")
        return self.face

    def get_face(self):
        """Get the face of the dice"""
        return self.face
