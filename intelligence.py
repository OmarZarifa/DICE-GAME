class Intelligence:
    def init(self, level):
        self.level = level

    def decide(self, player_score, opponent_score):
        if self.level == "easy":
            self.easy_level(player_score)
            
        elif self.level == "medium":
            self.medium_level(player_score, opponent_score)
        
        elif self.level == "hard":
            self.hard_level(player_score, opponent_score)


    def easy_level(self, player_score):
        if player_score < 20:
            return "roll"
        else:
            return "hold"

    def medium_level(self, player_score, opponent_score):
        if player_score < 25:
            return "roll"
        elif player_score - opponent_score > 20:
            return "hold"
        else:
            return "roll"
        
    def hard_level(self, player_score, opponent_score):
        if player_score < 35:
            return "roll"
        elif player_score - opponent_score > 30:
            return "hold"
        else:
            return "roll"
