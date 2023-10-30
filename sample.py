class Wow:
    def __init__(self, n):
        self.n = n
@property
def n(self):
    return self.__n # mangled
@n.setter
def n(self, new_n):
    self.__n = new_n

if __name__ == '__main__':
    # remember EVERYTHING is an Object
    # All objects allow arbirary proerties to be added to them

    w = Wow(True)
    # it appears liek we can set w.__n
    w.__n = 'can this really happen?'
    w.here_is_some_arbitrary_proerpty = 'rubbish' # this is always possible
    print(w.__n) # seems to work, but its just another arbitrary property
    print(w.n) # this accesses the ACTUAL __n value