class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, score):
        self.score += score

    def reset_score(self):
        self.score = 0

    def set_name(self, new_name):
        self.name = new_name
        print(f"Your new name is {new_name}, you can continue your playing by this name ")

    def __str__(self):
        return self.name
