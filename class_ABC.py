# Python offers an Abstract Base Class
from abc import ABCMeta, abstractmethod, abstractproperty # see PEP8

# usualy in Python we use ABCMeta like this
class MyAbstract(metaclass=ABCMeta):
    '''An abstract class lets us specify any properties and methods without implementation'''
    name = 'ooh look we can declare anything as a prop (even ouside the __init__)'
    @abstractmethod
    def someMethod(self, point):
        '''Take an instance of a point and do stuff with it'''

# Next we would use this in a concrete  (usually in a separate module)
class MyConcrete(MyAbstract):
    '''A concrete class will be one we actually use in code
    It must implement actual functionality'''
    def someMethod(self, point):
        return point.x*2 # do something concrete with the provided data
    
class MyOther(MyAbstract):
    pass # in Python we are NOT obliged to honour the abstract class
    # but ABC helps us remember to implement concrete examples of the abstract members
    def someMethod(self, point):
        return point.x/2
    
# simple inheritance
# by efault EVERY class inherits from object
class Q(): # this implicitly inherits from object
    pass
class M: # this implicitly inherits from object
    pass
class N(object): # here we explicitly inherit from object
    pass




if __name__ == '__main__':
    c1 = MyConcrete()
    c2 = MyOther() # no problem