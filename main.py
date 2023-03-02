from game import Game
from intelligence import Intelligence
def main():
        print("Welcome to Pig Dice Game!")
        print("1. Play against the computer")
        print("2. Play against another player")
        print("3. View rules")
        print("4. Quit")
        
        choice = 3
        while (choice == 3):
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                name = input("Please enter your name: ")
                level = input("Select computer intelligence level (dumb, medium or hard): ")
                game =  Game(name, "computer")
                game.computer_playing(level)

            elif choice == 2:
                name1 = input("Enter the name of the first player: ")
                name2 = input("Enter the name of the second player: ")
                game = Game(name1, name2)
                game.human_playing()


            elif choice == 3:
                print('Welcome to Pig Dice!\n')
                print('The objective of the game is to be the first player to score 100 points.')
                print('On each turn, a player rolls a six-sided die as many times as they want and the sum of the dice rolls is added to their score for the round.')
                print('However, if the player rolls a 1, their score for the round is reset to 0 and their turn ends.')
                print('The player can choose to hold at any time, which adds their round score to their total score and ends their turn.')
                print('Good luck!\n') 
        
            elif choice == 4:
                print("Good bye :)")
        
main()
