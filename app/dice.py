import random


class Dice:
    def __init__(self):
        self

    def roll(self):
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
