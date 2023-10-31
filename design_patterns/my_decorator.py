# we have met some built in decorators
# @property, @abstractmethod....

def showArgs(f):
    '''this function can be used to decorate ANY otehr function
    Decorators add functionality to an existing function'''
    def newFunc(*args, **kwargs):
        print(f'Running a function called {f.__name__}')
        print(f'The positional arguments are {args}')
        print(f'The keyword arguments are {kwargs}')
        return f(*args, **kwargs)
    return newFunc # we dont call it here

@showArgs # use the custom decorator
def isOdd(n):
    return n%2 == 1 # True if odd, False if not odd

if __name__ == '__main__':
    isOdd(3) # True
    isOdd(n=4)