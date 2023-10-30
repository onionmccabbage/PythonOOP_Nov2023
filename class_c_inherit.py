# Consider a point in 3-d space. It will have x and y (like the 2d point)
# we also need z for 3-d space

import class_b
# or
from class_b import Point2D
# we can now use our class to make other classes
class Point3D(Point2D): # inherit from Point2D
    '''we can add a property for z'''
    def __init__(self, x, y, z):
        # we typically call the __init__ method of the parent class
        super().__init__(x, y) # we now have an instance of a Point2D
        self.z = z
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, new_z):
        if type(new_z) in (int, float):
            self.__z= new_z
        else:
            raise TypeError('z must be a number')
    def __str__(self):
        msg = super().__str__()
        return f'{msg} z={self.z}'

print(__name__) # we try not to polute the global namespace

if __name__ == '__main__':
    # ''' we have access to everything inside 'class_b' '''
    '''we have access to the Point2D class'''
    # p = class_b.Point2D(5, 6)
    p = Point3D(5, 6, 2)
    p.y = 99
    print(p) # this will use our __str__ method