import sys
sys.path.insert(0, './Classes/')
sys.path.insert(0, './json/')
sys.path.insert(0, './Saves/')

import classes as cl
import functions as func
import entities as ent
import copy as cp

import os
import random as rand

def main():
    choice = 0
    while choice not in [1,2]:
        func.clr()
        s = func.Center("Trivia Knight\nTurn-based Rougelike Trivia RPG\n\n\n" + 
        func.TableDisplay([
            ["[1]", "New Game"],
            ["[2]", "Load Game"],
            ["[3]", "Leaderboard"],
            ["[4]", "How to Play"],
            ["[0]", "Exit"]
        ], [-1,-1], border = " "
        ) + "\n\n\nEnter Choice: ", vert=True)

        choice = func.loopValidChoice(range(0,5), text = s)
        
        if choice == 0:
            return None
        elif choice == 1:
            save = NewSave()
            gameMain()
        elif choice == 2:
            LoadSave()
        elif choice == 3:
            leaderboard()
        elif choice == 4:
            leaderboard()
        
def gameLoop(category, entities, wave):
    global save, player

    lambda x: 100**(-1/x.spd(x.level(wave)))-x.spd(x.level(wave))**0.6+100
    expG = sum([round(3*(x.level(x.wave))*(rand.random()**(1/2))) for x in entities])

    entities = [[x, x.spd(x.level(x.wave))] for x in entities]
    entities.sort(reverse=True, key = lambda x: x[1])

    turn = 1
    while len(entities) > 0:
        print("Turn " + str(turn))
        print("Turn Order")

        # display turn order
        i = 0
        p = False
        order = []
        disp = []
        while i < len(entities):
            if player.spd() >= entities[i][1] and not p:
                text = "("+ str(player.hp) +"/" + str(player.maxhp()) + ")"
                text = func.ProgressBar(player.hp, player.maxhp(), len(text)+5*2)[:5] + text + func.ProgressBar(player.hp, player.maxhp(), len(text)+5*2)[-5:]     

                r = [player.name + " (Lv. " + str(player.level)+ "):     ", text]
                disp.append(r)

                p = True
                order.append(-1)
            else:
                hp = entities[i][0].hp
                mhp = entities[i][0].maxhp(entities[i][0].level(wave))
                text = "("+ str(hp) +"/" + str(mhp) + ")"
                text = func.ProgressBar(hp, mhp, len(text)+5*2)[:5] + text + func.ProgressBar(hp, mhp, len(text)+5*2)[-5:]

                disp.append([entities[i][0].name +  " (Lv. " + str(entities[i][0].level(wave))+ ")   ", text])
                i+=1
                order.append(i)
        
        turn_order = func.Center("Turn " + str(turn) + "\nTurn Order\n\n"+func.TableDisplay(disp, [-1, -1], border=" "), vert = True, offsetY=(9+len(disp))//2-1)
        actionsD = func.Center(func.TableDisplay([["[1]", "Attack"], ["[2]", "Heal"], ["[3]", "Scan"]], [-1, -1], border = " ") + "\nAction: ")
        
        # action
        actions = []
        choice1 = 0
        while choice1 not in range(1, 3):
            choice1 = func.loopValidChoice(range(1,4), (turn_order + "\n"+actionsD))
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
        turn += 1
    
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
    displayStr = []
    for x in range(1,4):
        cats.append(rand.randint(0, len(categories)-1))
        text = cat_txts[cats[x-1]][rand.randint(0,len(cat_txts[cats[x-1]])-1)]
        displayStr.append(["[" + str(x) + "]", text + "   "])

    choice = func.loopValidChoice(range(1, 4), func.Center(func.TableDisplay(displayStr, [-1, -1], border = " ") + "\n\nChoose a Room: ", vert=True))

    return gameLoop(categories[cats[choice-1]], entities, wave)
    

def NewSave():
    global player

    a = True
    extraD = ""
    while a:
        func.clr()
        player_name = input(func.Center(extraD, vert = True, offsetY=4) + func.Center("\nEnter Player Name: ", offsetX = 7))
        confirm = input(func.Center("\nConfirm? (y/n) ", offsetX=1))
        while confirm != "y":
            func.clr()
            print(func.Center("Enter Player Name: ", vert = True, offsetY=3, offsetX=10) + player_name)
            confirm = input(func.Center("\nConfirm? (y/n) ", offsetX=1))

        #print(":&:" in player_name)
        if ":&:" in player_name:
            extraD = "Player Name Contains Special Characters. Try Again.\n\n"
            continue

        try:
            save_file = open("Saves/" + player_name + ".txt", "r")
        except:
            save_file = open("Saves/" + player_name + ".txt", "w")
            a = False
        else:
            extraD = "Player Name Already Taken. Choose Another.\n\n"
            continue
        
        player = cl.Player(player_name, 1)

    func.clr()
    save_file.write(player_name+"\n")
    save_file.write("1\n")
    save_file.write("0\n")

    save_file.close()

    saves = open("Saves/saves.txt", "a")
    if os.stat("Saves/saves.txt").st_size != 0:
        saves.write("\n")
    saves.write(player_name)
    saves.close()


def LoadSave ():
    global player
    
    if os.stat("Saves/saves.txt").st_size != 0:
        saves = open("Saves\saves.txt")
        save_list = []

        m = 0
        tab = []
        for i, x in enumerate(saves):
            if x[-1] == "\n":
                x = x[:-1]
            
            tab.append(["[" + str(i+1) + "]", x])
            save_list.append(x)
            m = i

        a = {1}
        a.update(set(range(1, m+1)))
        m = func.loopValidChoice(a, text = func.Center(func.TableDisplay(tab, [-1, -1], border = " ") + "\n\nSelect Save File: ", vert = True), clear=False) 

        save_file = open("./Saves/"+save_list[m-1]+ ".txt", "r")   

        player.name = save_file.readline()[:-1]
        player.level = int(save_file.readline())
        player.exp = int(save_file.readline())

        save_file.close()
        saves.close()

        input(func.Center(player.name + "'s file loaded."))
        gameMain()
    else:
        input("No Save Files Found.")

def Save():
    global player
    
    save_file = open("Saves/"+ player.name + ".txt" ,"w")
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
        # write to leaderboard
        leaderboard = open("Saves/leaderboard.txt","a")
        leaderboard.write(player.name + ":&:" + wave)
        leaderboard.close()

        #delete save file
        os.delete("Saves/"+player.name+".txt")
        
        #remove from saves

        saves = open("Saves/saves.txt", "r")
        s = []

        for x in saves:
            x.replace("\n", "")
            if x != player.name:
                s.append(x)
        
        saves.close()
        
        saves = open("Saves/saves.txt", "w")
        for x in s:
            saves.write(x)
            saves.write("\n")
        saves.close()
        

def leaderboard():
    leaderboard = open("Saves/leaderboard.txt")
    func.clr()

    leadL = []
    for x in leaderboard:
        a = x.split(":&:")
        a = [a[0], int(a[1])]
        leadL.append(a)
    
    leaderboard.close()

    leadL.sort(reverse = True,key=lambda a: a[1])

    strD = [["Rank", "Player", "Wave"]]
    for (ind,x) in enumerate(leadL):
        strD.append([str(ind+1), x[0], str(x[1])])
    
    input(func.Center(func.TableDisplay(strD, [-1, -1, -1], border = "     "), vert = True, offsetX = 0) + "\n\n")

player = cl.Player("", 1)
categories, cat_txts = func.initCategories()

main()
#leaderboard()
#func.askQuestion(rand.choice(categories), 0)
