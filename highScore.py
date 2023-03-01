class HighScore:
    def _init_(self):
        self.total_score = 0
    def add_score(self, current_score):
        self.total_score += current_score
    def get_score(self):
        return self.total_score
