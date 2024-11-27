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

    lambda x: 100**(-1/x.spd(x.level(wave)))-x.spd(x.level(wave))**0.6+100

    entities = [[x, x.spd(x.level(x.wave))] for x in entities]
    entities.sort(key = lambda x: x[1])

    i = 1
    while len(entities) > 0:
        print("Turn " + str(i))
        print("Turn Order")

        # display turn order
        i = 0
        p = False
        while i < len(entities):
            if player.spd() >= entities[i][1] and not p:
                text = "("+ str(player.hp) +"/" + str(player.maxhp()) + ")"
                print(player.name + ": "  + func.ProgressBar(player.hp, player.maxhp(), len(text)+5*2)[:5] + text + func.ProgressBar(player.hp, player.maxhp(), len(text)+5*2)[-5:])
                p = True
            else:
                hp = entities[i][0].hp
                mhp = entities[i][0].maxhp(entities[i][0].level(wave))
                text = "("+ str(hp) +"/" + str(mhp) + ")"
                print(entities[i][0].name + ": "  + func.ProgressBar(hp, mhp, len(text)+5*2)[:5] + text + func.ProgressBar(hp, mhp, len(text)+5*2)[-5:])
                i+=1
        
        # action
        actions = []
        choice = func.loopValidChoice(range(1,3), "\n[1] Attack\n[2] Item\nAction: ")
        actions.append(choice)
        if choice == 1:
            strDisplay = ""
            for i in range(len(entities)):
                hp = entities[i][0].hp
                mhp = entities[i][0].maxhp(entities[i][0].level(wave))
                text = "("+ str(hp) +"/" + str(mhp) + ")"
                print("[" + str(i + 1)+"] " + entities[i][0].name + ": "  + func.ProgressBar(hp, mhp, len(text)+5*2)[:5] + text + func.ProgressBar(hp, mhp, len(text)+5*2)[-5:])
            choiceAttack = func.loopValidChoice(range(1, len(entities) + 1), strDisplay + "Target: " )
            actions.append(choiceAttack)
            
            choice = func.loopValidChoice(range(1,4), "[1] Easy (x1) \n[2] Normal (x1.3) \n[3] Hard (x1.5)\nAction: ") - 1
            actions.append(choice)
            

        print("Turn Start!")
        i = 0
        pSpd = player.spd()
        while i < len(entities):
            if pSpd > entities[i][1]:
                if actions[0] == 1:
                    player.Attack(entities[actions[1]-1][0], category, actions[2])
                    if entities[actions[1]-1][0].hp <= 0:
                        entities.pop(actions[1]-1)
                        if choiceAttack - 1 < i:
                            i -= 1
            else:
                entities[i].Attack(player)
                i += 1
            if player.hp <= 0:
                return False      

    '''while len(entities) > 0:
        break
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
                    return False'''
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