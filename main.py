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
    func.clr()
    print("""Trivia Knight
Turn-based Rougelike Trivia RPG

[1] Start Game
[2] Load Game
[0] Exit
""")

    choice = func.loopValidChoice(range(0,3), text = "Enter Choice: ")
    
    if choice == 0:
        return None
    if choice == 1:
        save = NewSave()
        gameMain()
    if choice == 2:
        LoadSave()
        gameMain()
        
def gameLoop(category, entities, wave):
    global save, player

    lambda x: 100**(-1/x.spd(x.level(wave)))-x.spd(x.level(wave))**0.6+100
    expG = sum([round(3*(x.level(x.wave))*(rand.random()**(1/2))) for x in entities])

    entities = [[x, x.spd(x.level(x.wave))] for x in entities]
    entities.sort(reverse=True, key = lambda x: x[1])

    i = 1
    while len(entities) > 0:
        func.clr()
        print("Turn " + str(i))
        print("Turn Order")

        # display turn order
        i = 0
        p = False
        order = []
        while i < len(entities):
            if player.spd() >= entities[i][1] and not p:
                text = "("+ str(player.hp) +"/" + str(player.maxhp()) + ")"
                print(player.name + " (Lv. " + str(player.level)+ "): \t"  + func.ProgressBar(player.hp, player.maxhp(), len(text)+5*2)[:5] + text + func.ProgressBar(player.hp, player.maxhp(), len(text)+5*2)[-5:])
                p = True
                order.append(-1)
            else:
                hp = entities[i][0].hp
                mhp = entities[i][0].maxhp(entities[i][0].level(wave))
                text = "("+ str(hp) +"/" + str(mhp) + ")"
                print(entities[i][0].name +  " (Lv. " + str(entities[i][0].level(wave))+ "): \t"  + func.ProgressBar(hp, mhp, len(text)+5*2)[:5] + text + func.ProgressBar(hp, mhp, len(text)+5*2)[-5:])
                i+=1
                order.append(i)
        
        # action
        actions = []
        choice1 = 0
        while choice1 not in range(1, 3):
            choice1 = func.loopValidChoice(range(1,4), "\n[1] Attack\n[2] Heal\n[3] Scan \nAction: ")
            if choice1 == 1:
                actions.append(choice1)
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
            elif choice1 == 2:
                actions.append(choice1)
                choice = func.loopValidChoice(range(1,4), "[1] Easy (10%) \n[2] Normal (20%) \n[3] Hard (30%)\nAction: ") - 1
                actions.append(choice)
            elif choice1 == 3:
                for i in range(len(entities)):
                    print("[" + str(i + 1)+"] " + entities[i][0].name)
                choiceScan = func.loopValidChoice(range(1, len(entities) + 1), "Target: " ) -1
                e = entities[choiceScan][0]
                print(e.name)
                print("HP:", str(e.hp) +"/"+str(e.maxhp(e.level(e.wave))))
                print("ATK:", str(e.atkA()))
                print("DEF:", str(e.defA()))
                print("SPD:", str(e.spdA()))
                input()
                

        #actions = [choice, choiceAttack, diff]
            

        print("Turn Start!")
        for ind, i in enumerate(order):
            if i == -1:
                if actions[0] == 1:
                    print(player.name, "attacks!")
                    player.Attack(entities[actions[1]-1][0], category, actions[2])
                    if entities[actions[1]-1][0].hp <= 0:
                        print(entities[actions[1]-1][0].name, "died!")
                        entities.pop(actions[1]-1)
                if actions[0] == 2:
                    print(player.name, "casts Heal!")
                    player.Heal(category, actions[1])
            else:
                if i <= len(entities):
                    entities[i-1][0].Attack(player)
                else:
                    continue
            if player.hp <= 0:
                print(player.name, "died!")
                return False  
            input()
    
    print("Room Cleared!")
    print(player.name + " gained " + str(expG) + " EXP!")
    player.GainXP(expG)
    if player.hp < player.maxhp():
        player.hp += player.maxhp() * 0.5
        if player.hp > player.maxhp():
            player.hp = player.maxhp()
    Save()
    input()
    return True


def waveStart(wave):
    # category select

    entities = []

    if wave < 5:
        num = 1
        r = rand.random()
        if r >= 0.75:
            num = 2
        if r >= 0.95:
            num = 3
    elif wave < 7:
        num = 1
        r = rand.random()
        if r >= 0.5:
            num = 2
        if r >= 0.75:
            num = 3
    elif wave < 10:
        num = 2
        r = rand.random()
        if r >= 0.75:
            num = 3
    else:
        num = 3
    

    
    for x in range (num):
        i = rand.randint(1, 9)
        entities.append(cp.deepcopy(ent.normal_enemies[i]))
        entities[x].SetWave(wave)
    
    '''
    entities.append(cp.deepcopy(ent.normal_enemies[1]))
    entities[0].SetWave(wave)
    entities.append(cp.deepcopy(ent.normal_enemies[2]))
    entities[1].SetWave(wave)
    entities.append(cp.deepcopy(ent.normal_enemies[7]))
    entities[2].SetWave(wave)
    '''

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

    a = True
    while a:
        player_name = input("Enter Player Name: ")
        while input("Confirm? (y/n)") != "y":
            player_name = input("Enter Player Name: ")

        if ":&:" in player_name:
            continue

        try:
            save_file = open("Saves/" + player_name + ".txt", "r")
        except:
            save_file = open("Saves/" + player_name + ".txt", "w")
            a = False
        else:
            print("Player Name Already Taken. Choose Another.")
            continue
        
        player = cl.Player(player_name, 1)

    cls()
    save_file.write(player_name+"\n")
    save_file.write("1\n")
    save_file.write("0\n")

    save_file.close()


def LoadSave ():
    global player

    save_file = open("Saves\"" + player.name + ".txt", "r")
    player.name = save_file.readline()
    player.level = int(save_file.readline())
    player.exp = int(save_file.readline())

    save_file.close()

def Save():
    global player

    save_file = open("Saves\""+ player.name + ".txt" ," w")
    save_file.write(player.name + "\n")
    save_file.write(str(player.level)+"\n")
    save_file.write(str(player.exp)+"\n")
    save.close()

def gameMain():
    nextWave = True
    wave = 0
    while nextWave == True:
        wave += 1
        nextWave = waveStart(wave)
    
    if nextWave==False:
        leaderboard = open("Saves/leaderboard.txt","a")
        leaderboard.write(player.name + ":&:" + wave)

def leaderboard():
    pass
    

player = None
categories, cat_txts = func.initCategories()

main()