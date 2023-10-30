from review_class import NumberFun
from datetime import datetime

class ExtendedNumberFun(NumberFun):
    def __init__(self, num, flag):
        super().__init__(num)
        self.flag = flag # could use get/set methods
    def __str__(self):
        txt = super().__str__()
        if self.flag == True:
            d = self.__dict__
            return txt + f'\nClass dictionary contains {d}'
        else:
            return txt

if __name__ == '__main__':
    r = ExtendedNumberFun(100, True)
    print(r)