from app.shell import Shell

if __name__ == '__main__':
    print("Welcome to Pig Dice Game!")
    print("")

    print("Enter 'start 1' to play against the computer")
    print("Enter 'start 2' to play against another player")
    
    # Create command object
    shell = Shell()
    
    # Start game
    shell.cmdloop()
