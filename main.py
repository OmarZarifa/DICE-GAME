"""The main class."""

from app.shell import Shell

if __name__ == '__main__':
    row1 = 46 * "-"
    row2 = 26 * "-"
    row3 = 46 * "="
    print(f"+{row2}+")
    print("| Welcome to Pig Dice Game |")
    print(f"+{row2}+")
    print("")
    print("+-------+   +-------+   +-------+   +-------+   +-------+   +-------+")
    print("|       |   | O     |   | O     |   | O   O |   | O   O |   | O   O |")
    print("|   O   |   |       |   |   O   |   |       |   |   O   |   | O   O |")
    print("|       |   |     O |   |     O |   | O   O |   | O   O |   | O   O |")
    print("+-------+   +-------+   +-------+   +-------+   +-------+   +-------+")
    print("")
    print(f"*{row3}*")
    print("|Enter 'start 1' to play against the computer  |")
    print(f"*{row1}*")
    print("|Enter 'start 2' to play against another player|")
    print(f"*{row3}*")
    print("")
    print("Help!")
  
    # Create command object
    shell = Shell()
    # Start the main game loop
    shell.cmdloop()
