# functional programming uses functions rather than classes
# (no absolute need for a class)

def isOdd(n):
    '''return True if odd, False if not'''
    return n%2 != 0 # ==, <, >, <=, >=, !=

def addThem(m ,n):
    return m+n

if __name__ == '__main__':
    '''we need to check odd or even for a bunch of values '''
    results = map(isOdd, range(-10, 11)) # start, stop-before
    print( type(results) ) # we have a 'map' object
    # we can iterate over the map object
    print(results.__next__())
    for r in results:
        print(f'Odd: {r}')


    matching = filter(isOdd, range(-10, 11))
    print( matching.__next__() )
    for m in matching:
        print(m, end=", ") # we can change the default end-character for 'print'
