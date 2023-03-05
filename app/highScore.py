class HighScore:
    def __init__(self):
        self.players_name = []
        self.players_score = []

    def add_score(self, score):
        self.players_score.append(score)

    def add_name(self, name):
        self.players_name.append(name)

    def display(self):
        # Print the table headers
        print("{:<10} {:<10}".format("Player", "Score"))
        print("=" * 20)

        # Print the table rows
        for i in range(len(self.players_name)):
            print("{:<10} {:<10}".format(self.players_name[i], self.players_score[i]))
