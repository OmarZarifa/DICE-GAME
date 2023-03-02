class Intelligence:
    def __init__(self, level):
        self.level = level

    def decide(self, round_score, total_score):
        if self.level == "dumb":
            return self.dumb_level()
            
        elif self.level == "medium":
            return self.medium_level(round_score)
        
        elif self.level == "hard":
            return self.hard_level(round_score, total_score)


    def dumb_level(self):
        return "roll"
    
    def medium_level(self, round_score):
        if round_score < 35:
            return "roll"
        else:
            return "hold"

        
    def hard_level(self, round_score, total_score):
        if round_score < 20 and total_score < 50:
            return 'roll'
        elif round_score < 15 and total_score >= 50:
            return 'roll'
        else:
            return 'hold'