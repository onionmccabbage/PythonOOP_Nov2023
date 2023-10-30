# we try to avoid globals but sometimes...
count = 0

def addOne():
    '''add one to the global count'''
    # we can refer to a ember on the global namespace like this
    global count
    count += 1 # Python shortcut syntax

def subtractOne():
    '''substract one from the gobal count'''
    global count
    count -= 1

if __name__ == '__main__':
    # here is a loop
    for i in range(0,10):
        addOne()
        print(count)
        subtractOne()
        print(count)