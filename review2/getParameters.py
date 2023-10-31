class AskUser():
    '''Ask the user for which ID they would like
       Validate it is a positive integer'''
    def __init__(self):
        pass
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, id):
        if int(float(id)) >= 0:
            self.__userId = id
            # break
    def askUser(self):
        whichId = ''
        while type(whichId) !=int:
            whichId = input('Enter an ID for user: ')
            if whichId.isnumeric():
                whichId = int(float(whichId))
        return whichId    
if __name__ == '__main__':
    ask = AskUser()
    ask.userId = ask.askUser()