import sys
sys.path.insert(0, './Classes/')
sys.path.insert(0, './json/')
sys.path.insert(0, './Saves/')
sys.path.insert(0, './Questions/')

import classes as cl
import functions as func

def main():
    print("""Trivia Knight
Rougelike-RPG based on Trivia

[1] New Game
[2] Load Game
[0] Exit
""")

    choice = func.loopValidChoice(range(0,3), "Enter Choice")
    
    if choice == 0:
        return None
    if choice == 1:
        NewSave()
    if choice == 2:
        LoadSave()
        

main()
