# we need to encapsulate the idea of a point in 2-d space
# the x and y values must be numeric

class Point:
    """This class will encapsulate a point in 2-d space
    x will be a number, y will also be a number"""
    # every method that belongs to a class MUST take 'self' as an argument
    def __init__(self, new_x, new_y): # this is the initializer for our class
        # in classes we typically use 'name mangling' __x
        self.x = new_x # we are setting the property of the isntance to the incoming value
        self.y = new_y # this will call the setter for y
    # here are some more methods of this class (a method is simple a function that is inside a class)
    def set_x(self, new_x): # setter or mutator
        '''check to make sure new_x is a number'''
        if (new_x.isnumeric()): # careful isnumeric only checks string values  # type(new_x)==float
            self.__x = float(new_x) # cast teh string to a floating point value
        else:
            raise TypeError() # or we could set a default
    def get_x(self): # getter or accessor
        return self.__x
    def set_y(self, new_y): # setter or mutator
        '''check to make sure new_y is a number'''
        if (new_y.isnumeric()): # careful isnumeric only checks string values  # type(new_x)==float
            self.__y = float(new_y) # cast teh string to a floating point value
        else:
            raise TypeError() # or we could set a default
    def get_y(self): # getter or accessor
        return self.__y   
    # we can make these get/set methods behave like properties
    x = property(get_x, set_x) # makes the functinos behave as properties
    y = property(get_y, set_y)

# __xxx__ is known as dunder
if __name__ == '__main__':
    # We can access intrinstic properties of any class
    print( Point.__doc__  ) # print the docstring
    # make instances of our class
    p1 = Point(3,4) # p1 is now an instance of the class
    p2 = Point(True, False) # every time we make an isntance, the __init__ is called
    # we call methods of a class like this (note the brackets)
    p2.x = '99' # set by using the setter method
    print(p2.x) # 99.0 access the value of x using the getter method
    print(p1.x, p1.y) # dot notation
    # print(p2[x], p2['y']) # square-bracket notation - fix this...
    # we can ask the user for values for the x and y
    x = input('Value of x? ') # every user input is ALWAYS a string
    y = input('Value of y? ')
    p3 = Point(x, y)
    print( p3.x, p3.y )