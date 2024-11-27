import sys
sys.path.insert(0, './Classes/')
sys.path.insert(0, './json/')
sys.path.insert(0, './Saves/')

import classes as cl
import functions as func
import entities as ent
import copy as cp

import random as rand

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
        
def gameLoop(category, entities, wave):
    global save, player

    entities.sort(key = lambda n: n.spd(n.level(wave)), reverse = True)

    while len(entities) > 0:
        playerMove = False
        i = 0
        while i < len(entities):
            if player.spd() >= entities[i].spd(entities[i].level(wave)) and playerMove == False:
                choice = func.loopValidChoice(range(1,3), "[1] Attack\n[2] Item\nAction: ")
                if choice == 1:
                    strDisplay = ""
                    for ind, j in enumerate(entities):
                        strDisplay += "[" + str(ind + 1) + "] " + j.name + " (HP: " + str(j.hp) + "/" + str(j.maxhp(j.level(j.wave))) + ")\n"
                    
                    choiceAttack = func.loopValidChoice(range(1, len(entities) + 1), strDisplay + "Target: " )
                    choice = func.loopValidChoice(range(1,4), "[1] Easy (x1) \n[2] Normal (x1.3) \n[3] Hard (x1.5)\nAction: ") - 1
                    
                    player.Attack(entities[choiceAttack-1], category, choice)
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
                if player.hp <= 0:
                    return False
    return True


def waveStart(wave):
    # category select

    entities = []
    for x in range (3):
        i = rand.randint(1, 9)
        entities.append(cp.deepcopy(ent.normal_enemies[i]))
        entities[x].SetWave(wave)

    cats = []
    displayStr = ""
    for x in range(1,4):
        cats.append(rand.randint(0, len(categories)-1))
        text = cat_txts[cats[x-1]][rand.randint(0,len(cat_txts[cats[x-1]])-1)]
        displayStr += "[" + str(x) + "] " + text + "\n"

    displayStr += "Choose a Room: "
    choice = func.loopValidChoice(range(1, 4), displayStr)

    return gameLoop(categories[cats[choice-1]], entities, wave)
    

def NewSave():
    global player

    player_name = input("Enter Player Name: ")
    player = cl.Player(player_name, 1)

def UploadSave ():
    global player

def gameMain():
    nextWave = True
    wave = 0
    while nextWave:
        wave += 1
        nextWave = waveStart(wave)
    


player = cl.Player("Test", 1)
save = None

categories, cat_txts = func.initCategories()

gameMain()