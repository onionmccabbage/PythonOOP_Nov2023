def makePositive(n=0): # we may choose to provide a default value
    '''return the positive part of any number'''
    return abs(n)

if __name__ == '__main__':
    '''exercise the code (only when run as the main module)'''
    for n in range(-4, 5, 1): # range() start,stop-before,step
        print(makePositive(n))
    # we can use the default
    print( makePositive() ) # 0