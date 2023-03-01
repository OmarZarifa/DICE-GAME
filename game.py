from dice import Dice
from player import Player


class Game:
    def __init__(self,name1, name2):
        self.dice = Dice()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        
        
    def play(self):
    
        while (self.p1.score<100 and self.p2.score<100):
            self.p1.rolling()
            answer = input("Restart (y/n) ?")
            if answer == "y":
                self.restart()
                
            else:
                if self.p1.score<100:
                    self.p2.rolling()
                    answer = input("Restart (y/n) ?")
                    if answer == "y":
                        self.restart()
                
                        
        if (self.p1.score>self.p2.score):
            print (f"{self.p1.name} wins!")
        else:
            print (f"{self.p2.name} wins!")
            
            
    def restart(self):
        self.p1.score = 0
        self.p2.score = 0
