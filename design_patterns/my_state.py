# state is an efficient design pattern, 
# since it is often more efficient to create a new state than
# mutate an existing one

class ComputerState():
    name='state'
    allowed = [] # a list of permitted state changes
    def switch(self, new_state):
        if new_state.name in self.allowed:
            print(f'Current state {self} switching to {new_state}')
            self.__class__ = new_state
        else:
            print(f'Current state {self} cannot switch to {new_state}')
            return self.name 

# A laptop can be Off, On, Sleep and Hybernate
class On(ComputerState):
    name='On'
    allowed = ['Off', 'Sleep', 'Hybernate']

class Off(ComputerState):
    name='Off'
    allowed = ['On']

class Sleep(ComputerState):
    name='Sleep'
    allowed = ['On']

class Hybernate(ComputerState):
    name='Hybernate'
    allowed = ['On']

class Laptop():
    def __init__(self, brand):
        self.brand = brand
        self.state = Off() # an instanvce of the Off state
    def change(self, change_to):
        self.state.switch(change_to)

if __name__ == '__main__':
    c = Laptop('Wizzy')
    c.change(On)
    c.change(Off)
    c.change(On)
    c.change(Sleep)
    c.change(On)
    c.change(Hybernate)
    c.change(Off) # should not work
