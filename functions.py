import sys
sys.path.insert(0, './Questions/')
sys.path.insert(0, './Classes/')
import random
import classes as cl
import math

# minor functions
def loopValidChoice(ran, text=''):
    print(text)
    x = input()
    print("\n")
    while not (x.isdigit() and int(x) in ran):
        x = input()
        print("\n")
    
    return int(x)

# questions

def initCategories():
    categories = []
    f = open('Questions/categories.txt', 'r')

    for x in f:
        categories.append(x)
    f.close()

    categories = list(categories)
    categories = [x[:-1] for x in categories]

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
#print(cat_txt)

    f.close()

    return categories, cat_txt



def askQuestion(category, difficulty):
    diffTxt = ["E", "M", "H"]
    fq = open("Questions/" + category + "_" + diffTxt[difficulty] +"_Q.txt", 'r')
    fa = open("Questions/" + category +  "_" + diffTxt[difficulty] +"_A.txt", 'r')

    qlist = []
    alist = []

    for x in fq:
        qlist.append(x[0:-1])
    for x in fa:
        alist.append(x[0:-1])

    num = random.randint(0, len(qlist)-1)
    q = qlist[num]
    a = alist[num]

    ans = input(q + "\n")

    fq.close()
    fa.close()

    if ans == a:
        return True
    else:
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