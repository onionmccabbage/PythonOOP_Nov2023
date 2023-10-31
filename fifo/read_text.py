def readFromTextFile():
    '''read and display all the text in a file'''
    try:
        fin = open('log.txt', 'r') # 'r' will let us read
        # r   = fin.read() # read all the text
        # r   = fin.readline() # read a line of the text (up to a line break)
        r   = fin.readlines() # read all the text as a lit of lines
        return r # we must remember to return something!
    except Exception as err: # we could catch specific exception types
        print(f'oops {err}')

if __name__ == '__main__':
    result = readFromTextFile()
    print(result)