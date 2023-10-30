# we need to encapsulate the idea of a point in 2-d space
# the x and y values must be numeric

class Point:
    """This class will encapsulate a point in 2-d space
    x will be a number, y will also be a number"""
    # every method that belongs to a classMUST take 'self' as an argument
    def __init__(self, new_x, new_y): # this is the initializer for our class
        self.x = new_x # we are setting the property of the isntance to the incoming value
        self.y = new_y

# __xxx__ is known as dunder
if __name__ == '__main__':
    # We can access intrinstic properties of any class
    print( Point.__doc__  ) # print the docstring

    # make instances of our class
    p1 = Point(3,4) # p1 is now an instance of the class
    p2 = Point(-3, -4) # every time we make an isntance, the __init__ is called
    print(p1.x, p1.y) # dot notation
    # print(p2[x], p2['y']) # square-bracket notation - fix this...