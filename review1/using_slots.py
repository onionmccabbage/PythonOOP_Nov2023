
class River():
    '''We capture attributes of a river'''
    # we can use named slots to restrict the members of our class
    __slots__ = ('start', 'end', 'coord', 'length')
    def __init__(self, start, end, coord, length):
        '''properties of this class'''
        self.start     = start # start will be a tuple of x/y coordinates
        self.end       = end   # end will be a list of x/y coordinates
        self.coord     = coord # at scale, rough lat/long (tuple)
        # self.sinuosity = sinuosity # we can derive this property
        self.length    = length
    # we also need methods of this class - things it migth do
    def flow(self):
        '''characterise the flow of the river'''
    def sinuosity(self):
        ''' derive from length, start, end etc.'''
    # we would then provide get/set methods to handle name-mangled values\

if __name__ == '__main__':
    # mutable version
    gade = River((3,5), [7,9], (4,8), 42.42 )
    gade.end = [8,9]
    # stateful version
    bulbourne = River((3,5), (7,9), (4,8), 42.42 ) # original instance
    bulbourne = River((3,5), (7,9), (8,9), 42.42 ) # replace with an entirely nes instance (a state)
    gade.__arb = 'we can always add any old arbitrary property to our class instance'
