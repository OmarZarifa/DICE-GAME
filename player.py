from dice import Dice


class Player:
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.dice=Dice(6)
        

    def set_name(self, new_name):
        self.name = new_name

    def rolling(self):
        if self.name != "computer":
            self.human_play()
        else:
            self.computer_play()

    def human_play(self):
        round_score=0
        again='y'
        #establish a while loop for the player's turn
        while again=='y':
            self.dice.roll()
            roll=self.dice.face
            if roll==1:
                print ('{} rolled a 1'.format(self.name))
                round_score=0
                again='n'
            else:
                print( '{} rolled a {}'.format(self.name,roll))
                round_score=round_score+roll
                print( "{}'s round score is {}".format(self.name,round_score))
                again=input(f"{self.name} do you want to roll again (y/n)? ")

                    
        self.score+=round_score
        print ("{}'s turn is over".format(self.name))
        print( "{}'s total score is {}\n\n".format(self.name,self.score))
        
    def computer_play(self):
        round_score=0
        again='y'
        #establish a while loop for the computer's turn
        while again=='y':
            self.dice.roll()
            roll=self.dice.face
            if roll==1:
                print ('{} rolled a 1'.format(self.name))
                round_score=0
                again='n'
            else:
                print( '{} rolled a {}'.format(self.name,roll))
                round_score=round_score+roll
                if round_score < 20:
                    print( '{} will roll again'.format(self.name))
                else:
                    again='n'     
        self.score+=round_score
        print( 'Turn is over')
        print( "{}'s round score is {}".format(self.name,round_score))
        print( "{}'s total score is {}\n\n".format(self.name,self.score))
