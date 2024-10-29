import sys
sys.path.insert(0, './Questions/')
import random

# minor functions
def loopValidChoice(ran, text=''):
    x = input(text)
    while not (x.isdigit() and x in ran):
        x = input(text)
    
    return int(x)

# questions

def initCategories():
    f = open('Questions/categories.txt', 'r')

    for x in f:
        categories.append(x)
    f.close()

def askQuestion(category):
    fq = open("Questions/" + category + "Q.txt", 'r')
    fa = open("Questions/" + category + "A.txt", 'r')

    qlist = []
    alist = []

    for x in fq:
        qlist.append(x[0:-1])
    for x in fa:
        alist.append(x[0:-1])

    num = random.randint(0, len(qlist))
    q = qlist[num]
    a = alist[num]

    ans = input(q + "\n")

    fq.close()
    fa.close()

    if ans == a:
        return True
    else:
        return False
    

categories = []
initCategories()