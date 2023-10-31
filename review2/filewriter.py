class FileWriter():
    def writeToFile(self, n, t_l):
        try:
            fout = open(n, 'a') 
            fout.writelines(t_l) # expects a list
            fout.close()
        except Exception as err:
            '''typically we would write our exceptino to a log file'''
            print(f'Something went wrong {err}')

if __name__ == '__main__':
    f = FileWriter()
    f.writeToFile('data.txt', ['a', 'b', 'c'])