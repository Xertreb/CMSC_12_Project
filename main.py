import sys
sys.path.insert(0, './Classes/')
sys.path.insert(0, './json/')
sys.path.insert(0, './Saves/')

import classes as cl
import functions as func

def main():
    print("""Trivia Knight
Turn-based Rougelike Trivia RPG

[1] Start Game
[2] Load Game
[0] Exit
""")

    choice = func.loopValidChoice(range(0,3), "Enter Choice: ")
    
    if choice == 0:
        return None
    if choice == 1:
        save = NewSave()
        gameMain()
    if choice == 2:
        LoadSave()
        
def gameMain():
    global save, player
    entities = []
    entities.append(cl.Unit("Rat", 3, 10, 5, 3, 1, 1))
    entities.append(cl.Unit("Rat", 3, 10, 5, 5, 3, 1))
    #entities.append(waveStart())

    entities.sort(key = lambda n: n.spd(), reverse = True)

    while len(entities) > 0:
        playerMove = False
        i = 0
        while i < len(entities):
            if player.spd() >= entities[i].spd() and playerMove == False:
                choice = func.loopValidChoice(range(1,3), "[1] Attack\n[2] Item\nAction: ")
                if choice == 1:
                    strDisplay = ""
                    for ind, j in enumerate(entities):
                        strDisplay += "[" + str(ind + 1) + "] " + j.name + " (HP: " + str(j.hp) + "/" + str(j.maxhp) + ")\n"
                    
                    choiceAttack = func.loopValidChoice(range(1, len(entities) + 1), strDisplay + "Target: " )

                    player.Attack(entities[choiceAttack-1], "General Knowledge")
                    if entities[choiceAttack-1].hp <= 0:
                        entities.pop(choiceAttack-1)
                        if choiceAttack -1 < i:
                            i -= 1
                else:
                    pass
                
                playerMove = True
            else:
                entities[i].Attack(player)
                i += 1


def waveStart():
    pass

def NewSave():
    global player

    player_name = input("Enter Player Name: ")
    player = cl.Player(player_name, 1)

def UploadSave ():
    global player


player = cl.Player("Test", 1)
save = None
gameMain()