def loopValidChoice(ran, text=''):
    x = input(text)
    while not (x.isdigit() and x in ran):
        x = input(text)
    
    return int(x)