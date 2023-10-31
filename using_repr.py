class Shape():
    '''a shape object'''
    def __init__(self, start, end):
        self.start = start
        self.end   = end
    # we need to pretty-print the shape
    def __repr__(self):
        '''This function will be used by any call for output in immediate-mode python'''
        return f'Point starts at {self.start} ends at {self.end}'  

if __name__ == '__main__':
    s = Shape( (3,4), (6,7) )
    s.__repr__()