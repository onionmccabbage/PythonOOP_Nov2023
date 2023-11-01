from threading import Thread
import random
import time

# functional threading
def someFn(n):
    '''this funtion will simply sleep for a random time'''
    for i in range(0,10):
        time.sleep( random.random()*0.1 )
        print(f'thread {n} is sleeping')

class SomeClass(Thread):
    '''this class inherist from Thread, so it can be run as a thread'''
    def __init__(self, n):
        Thread.__init__(self) # call the parent class (Thread)
        self.n = n
    def run(self):
        '''we override the run method of Thread'''
        for i in range(0,10):
            time.sleep( random.random()*0.1 )
            print(f'class thread {self.n} is sleeping')

if __name__ == '__main__':
    ''' we can target ANY function to be run as a new thread'''
    t1 = Thread(target=someFn, args=(1,)) # a one member tuple
    t2 = Thread(target=someFn, args=(2,)) # a one member tuple
    # use our class threads
    c1 = SomeClass('A')
    c2 = SomeClass('B')
    t1.start()
    t2.start()
    c1.start()
    c2.start()
    # it is a good idea to join threads
    t1.join()
    t2.join()
    c1.join()
    c2.join()