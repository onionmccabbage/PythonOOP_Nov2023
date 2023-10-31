from my_decorator import showArgs

@showArgs
def river(start_tup, end_tup, length_f, name_s):
    return f'''The river {name_s} is {length_f} long
It begins at x:{start_tup[0]} y:{start_tup[1]}
It ends at x:{end_tup[0]} y:{end_tup[1]}'''

if __name__ == '__main__':
    r = river((3,2), (6,4), 42435, 'ooblywoob' )
    print(r)