import sys

print(sys.maxsize) # the largest object that can exist in memory
print(sys.float_info)

num = 1.235567789

# we can format nubmers within strings
print(f'number is about {num:0.2f}')

def howBig():
    '''Python can deal with very very large numbers'''
    print(10**1000000)

if __name__ == '__main__':
    ''''''
    # howBig()