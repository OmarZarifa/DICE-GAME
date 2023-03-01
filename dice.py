import random

class Dice:
    def __init__(self,n=6):
        self.sides=n
        self.roll()
        
    def roll(self):
        self.face=int(random.random()*self.sides+1)
