import random

class Dice:
    def __init__(self):
        self
        
    def roll(self):
        self.face= random.randint(1, 6)
        if self.face == 1:
            print("┌─────────┐")
            print("│         │")
            print("│    ●    │")
            print("│         │")
            print("└─────────┘")
            
        elif self.face == 2:
            print("┌─────────┐")
            print("│  ●      │")
            print("│         │")
            print("│      ●  │")
            print("└─────────┘")
            
        elif self.face == 3:
            print("┌─────────┐")
            print("│  ●      │")
            print("│    ●    │")
            print("│      ●  │")
            print("└─────────┘")

        elif self.face == 4:
            print("┌─────────┐")
            print("│  ●   ●  │")
            print("│         │")
            print("│  ●   ●  │")
            print("└─────────┘")
      
        elif self.face == 5:
            print("┌─────────┐")
            print("│  ●   ●  │")
            print("│    ●    │")
            print("│  ●   ●  │")
            print("└─────────┘")

        elif self.face == 6:
            print("┌─────────┐")
            print("│  ●   ●  │")
            print("│  ●   ●  │")
            print("│  ●   ●  │")
            print("└─────────┘")
            
        else:
            print("┌─────────┐")
            print("│         │")
            print("│         │")
            print("│         │")
            print("└─────────┘")
        return self.face
            
        

 


