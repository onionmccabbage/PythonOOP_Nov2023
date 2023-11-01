
def genSq():
    '''Generate an endless sequence of square nubmers'''
    n=1
    while True: # careful with endless loops...
        sq = n*n
        n += 1
        yield sq # the yield statement makes this function into a generator

if __name__ == '__main__':
    g = genSq() # we have an instance of our generator
    print(type(g)) # we have a generator
    # we can access each member in turn (each member will be generated)
    print( g.__next__() ) # 1
    print( g.__next__() ) # 4
    print( g.__next__() ) # 9
    print( g.__next__() ) # 16

    # we can iterate over a generator (picks up from the next value)
    for s in g:
        print(s, end=', ')
        if s>100:
            break # breaks out of a loop
    
    print(g.__next__()) # 144, the next value!
