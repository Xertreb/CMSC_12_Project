import sys
sys.path.insert(0, './Questions/')
sys.path.insert(0, './Classes/')
import random
import classes as cl
import math
import os

def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# minor functions
def loopValidChoice(ran, text='', clear = True):
    x = "a"
    b = lambda x, ran: x.isdigit() and int(x) in ran
    while not b(x, ran):
        if clear:
            clr()
        if text != "":
            print(text, end = "")
        x = input()
    
    if clear == True: 
        clr()
    return int(x)

# questions

def initCategories():
    categories = []
    f = open('Questions/categories.txt', 'r')

    for x in f:
        categories.append(x)
    f.close()

    categories = list(categories)
    categories = [x[:-1] if x[len(x)-1] == "\n" else x for x in categories]

    f = open("Questions/category_text.txt", 'r')
    
    cat_txt = {}

    i = 0
    cat_txt[i] = []
    for x in f:
        x = x[:-1]
        if x != ":&:":
            cat_txt[i].append(x)
        else:
            i += 1
            cat_txt[i] = []
    
    del cat_txt[len(cat_txt.keys())-1]

    f.close()

    return categories, cat_txt



def askQuestion(category, difficulty):
    diffTxt = ["E", "M", "H"]
    fq = open("Questions/" + category + "_" + diffTxt[difficulty] +"_Q.txt", 'r')
    fa = open("Questions/" + category +  "_" + diffTxt[difficulty] +"_A.txt", 'r')

    qlist = []
    alist = []

    for x in fq:
        if x[len(x)-1] == "\n":
            qlist.append(x[0:-1])
        else:
            qlist.append(x)
    for x in fa:
        if x[len(x)-1] == "\n":
            alist.append(x[0:-1])
        else:
            alist.append(x)

    num = random.randint(0, len(qlist)-1)
    q = qlist[num]
    a = alist[num]

    clr()
    print(Center(ParagraphWrap(q, 50)+ "\n", vert=True))
    print(Center("", offsetX=25), end="")
    ans = input("")

    fq.close()
    fa.close()

    if ans.lower() == a.lower():
        return True
    else:
        clr()
        print(Center(ParagraphWrap(q, 50)+ "\n", vert=True))
        print(Center(ans, offsetX=20), end="\n\n")
        input(Center("Sorry! The correct answer was " + a+ "!"))
        return False

def ProgressBar (v, max, size=10):
    #[==========] 
    text = "["
    percent = v/max
    p1 = math.floor(percent * size)
    p2 = int(percent * size*100)/100
    
    text += "=" * int(p1)
    if p1 < p2:
        text += "-" 
        text += " " * int(size-p1-1)
    else:
        text += " " * int(size-p1)
    text += "]"
    return text

def TableDisplay(rows, sizes, border = "|"):
    for x in range(len(rows)):
        for y in range(len(sizes)):
            rows[x][y] = str(rows[x][y])
    
    for i, x in enumerate(sizes):
        if x == -1:
            for y in rows:
                sizes[i] = max(sizes[i], len(y[i]))
    strDisplay = ""
    for x in rows:
        rNeeded = 1
        for ind, y in enumerate(x):
            rNeeded = max(rNeeded, len(str(y)) // sizes[ind])
        
        i = 0
        while i < rNeeded:
            strDisplay += border
            j = 0
            while j < len(sizes):
                s = x[j][:sizes[j]]
                s += " " * (sizes[j] - len(s))
                x[j] = x[j][sizes[j]:]

                strDisplay += s
                strDisplay += border
                j += 1
            strDisplay += "\n"
            i += 1
    
    return strDisplay

def ParagraphWrap(text, size):
    words = text.split(" ")
    par = [[""]]

    i = 0
    for x in words:
        #print(par)
        if len(par[i][0] + " " + x) < size:
            #print(par[i])
            st = par[i].pop(0)
            par[i].append(0)
            par[i][0] = st + x + " "
        else:
            par.append([])
            i+=1
            par[i].append(x + " ")
    
    return TableDisplay(par, [size], border = "")
        

def Center(text, vert = False, hor = True, offsetY = 0, offsetX = 0):
    s = text.split("\n")

    cols = os.get_terminal_size().columns
    lines = os.get_terminal_size().lines
    disp = ""

    if vert:
        t = (lines - len(s)) // 2
        b = (lines - len(s)) // 2

        if t + b + len(s) > lines:
            b -= 1
        elif t + b + len(s) < lines:
            t += 1
        
        disp += "\n"*(t-offsetY)

    if hor: 
        for ind, x in enumerate(s):
            l = (cols - len(x)) // 2
            r = (cols - len(x)) // 2
            length = len(x)

            if l + r + length > cols:
                r -= 1
            elif l + r + length < cols:
                l += 1
            
            disp += " " * (l-offsetX) + x
            if ind != len(s) - 1:
                disp += "\n"
    return disp

def QueueOutputStr(disp, apd, spc = 2):
    disp.append(apd)
    s = ""
    for ind, x in enumerate(disp):
        s += x
        if ind + 1 != len(disp):
            s+= "\n" * spc

    clr()
    # print(disp)
    print(Center(s, vert= True), end="")
    input()