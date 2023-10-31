# the factory pattern
#Here is a top level class

class Animal():
    '''All creatues are kinds of Animal'''
    def makeANoise(self):
        pass

# here are some animals (usually each class is in a separate module)
class Dog(Animal):
    '''Dogs go 'woof' '''
    def makeANoise(self):
        return 'woof'
class Cat(Animal):
    '''Cats go 'miaow' '''
    def makeANoise(self):
        return 'miaow'
class Lion(Animal):
    '''Lions go 'roar' '''
    def makeANoise(self):
        return 'roar'
class Bat(Animal):
    '''Bats go '____' '''
    def makeANoise(self):
        return '____'
    
class CreatureFactory():
    '''This is a single point of access for any of the creatures we may need'''
    def make_sound(self, obj):
        # we sue eval to determine which class is needed
        return eval(obj)().makeANoise()
    
if __name__ == '__main__':
    cf = CreatureFactory()
    creature = input('Which creature? ') # always a string
    noise = cf.make_sound(creature)
    print(f'{creature} goes {noise}')
