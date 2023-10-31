# There are several ways to pesist text in a file
def printToFile(t):
    '''simply use print to output to a file'''
    # we use 'a' to append to a file (or create it)
    #        'x' for exclusive access (file must not exist)
    #        'w' (over)write every time
    #        't' means use text (default)
    # we should use try-except
    fout = open('log.txt', 'w') # this is a file access object
    # the print statement ALWAYS adds a new-line character
    print(t, file=fout) # direct the print to our file access object

# I/O is a blocking action - it takes a non trivial time to complete
def writeToFile(t):
    '''a more controlled approach to writing files
    NB it is always a good idea to catch potential exceptions'''
    try: # any exceptions can be caught
        fout   = open('log.txt', 'x') # file access object
        size   = len(t) # NB all strings of text have a len()
        offset = 0
        chunk  = 12 # choose twelve characters at a time
        while True: # be careful - this will loop endlessly
            if offset > size:
                fout.write('\n') # ad a new line at the end
                break # this will end the loop
            else:
                # we might choose to do other stuff (to avoid a feeling of blocking)
                part = t[offset:offset+chunk] # slicing [start:stop-before]
                fout.write(part) # write just 12 characters
                offset += chunk
        fout.close() # always a good idea to tidy up
    except Exception as err:
        '''typically we would write our exceptino to a log file'''
        print(f'Something wemt wrong {err}')


if __name__ == '__main__':
    text = 'is it time for coffee?'
    # printToFile(text)
    text = 'Here is a great big long amount of very dull text which needs to be persisted into a file by means of the fucntinos in this module'
    writeToFile(text)