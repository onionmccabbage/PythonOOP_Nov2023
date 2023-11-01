# there are loads of parts of pythno e can override

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, other):
        '''make a case-insensitive equality comparison'''
        return self.text.lower() == other.text.lower()
    
if __name__ == '__main__':
    # normal string comparison
    w = 'hello'
    x = 'Hello'
    print( w==x ) # False
    m = Word('hello')
    n = Word('Hello')
    print( m==n ) # this uses our overriden __eq__ therefore True

# other built-ins
# __eq__ __neq__, __gt__, __lt__, __ge__, __lt__
# __add__ __mult__ __sub__ __div__