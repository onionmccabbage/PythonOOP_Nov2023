# every python file is called a 'module'
# in Python everything is an object (even modules)

class Point2D:
    '''Here we represent a point by x an y (numbers)'''
    def __init__(self, x, y):
        self.x = x # now we will use our setter method
        self.y = y
    # we can declare get/set methods using decorator syntax
    @property # this is a simple way to make a function behave like a property
    def x(self):
        '''we could check that this environment is permitted to access __x'''
        return self.__x # this can be referred to as _Point2D__x
    @x.setter
    def x(self, new_x):
        '''only allow valid numbers for x'''
        # if type(new_x)==int or type(new_x)==float:
        if type(new_x) in (int, float): # the type l=must be int or float
            self.__x = new_x
        else:
            self.__x = 1  # a sensible default
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y) in (int, float):
            self.__y = new_y
        else:
            self.__y = 1 # sensible default (could raise an exception)
    # we can override the built-in method __str__
    def __str__(self):
        '''The __str__ method is ALWAYS used by 'print()' '''
        # return str((self.x, self.y)) # a tuple calling the getter methods
        # we can use string formatting syntax
        return f'Point x={self.x} y={self.y}' # curly-brackets inject valuess
    # we can derive values 
    def hypot(self):
        '''Return the hypotenuse given z and y
        h=(x*x+y*y)**0.5'''
        h = (self.x**2 + self.y**2)**0.5
        return h # we choose not to persist h, since it can always be derived
    def __getitem__(self, item): # emulate square-bracket syntax
        '''allow square-bracket access to class members'''
        return self.__dict__['_Point2D__x']

if __name__ == '__main__':
    '''we can make instances of our class'''
    t = Point2D(True, 4) 
    # try square-bracket access
    print(f'If we implement __getitem__() we can use square bracket syntax: {t["x"]}')
    print(t.x) # this will call the function that gets 'x'
    # if we REALLY need to we CAN access name-mangled properties
    # the pattern is always ._ClassName__prop
    print( f'We CAN access directly: {t._Point2D__x}' )
    print(t) # this must call the __str__ method
    # find th hypot
    q = Point2D(3,4)
    print( q.hypot() ) # 5.0