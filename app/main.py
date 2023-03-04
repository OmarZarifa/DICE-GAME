from shell import Command

if __name__ == '__main__':
    print("┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐")
    print("│         │  │  ●      │  │  ●      │  │  ●   ●  │  │  ●   ●  │  │  ●   ●  │")
    print("│    ●    │  │         │  │    ●    │  │         │  │    ●    │  │  ●   ●  │")
    print("│         │  │      ●  │  │      ●  │  │  ●   ●  │  │  ●   ●  │  │  ●   ●  │")
    print("└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘")
    print("┌─────────┐  ┌─────────┐  ┌─────────┐ ")
    print("│ ┌─────┐ │  └───┐ ┌───┘  │  ┌──────┘ ")
    print("│ └─────┘ |      │ │      │  │  ┌───┐ ")
    print("│ ┌───────┘  ┌───┘ └───┐  |  └────┘ | ")
    print("└─┘          └─────────┘  └─────────┘ ")
    print("")
    print("")
    print("Welcome to Pig Dice Game!")
    print("")
    print("")
    print("Enter 'start 1' to play against the computer")
    print("Enter 'start 2' to play against another player")
    
    # Create command object
    command = Command()
    
    # Start game
    command.cmdloop()
