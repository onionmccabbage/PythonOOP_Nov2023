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
        return self.__x
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
            self.__y == new_y
        else:
            self.__y = 1 # sensible default (could raise an exception)

if __name__ == '__main__':
    '''we can make instances of our class'''
    t = Point2D(False, 4) 
    print(t.x) # this will call the function that gets 'x'