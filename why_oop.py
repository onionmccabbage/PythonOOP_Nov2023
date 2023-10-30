# We only use classes when nothing else will do
# There are plenty of structures in Python...
a = 1 # integer
b = 2.3 # floating point
a = 5.99 # Python is dynamically typed
a = True # boolean (False)
s = 'welcome' # a immutable string of characters. This is a collection
# s[0] = 'W' # will not work
print( s[5] )
# other collections
# tuple is an immutable collection of any data types
t = (4, 7.5, 'hello', True, s , b )
print(t, type(t), t[2:5]) # slicing: [start:stop-before:step]
# list is a mutable collection of any data types
l = [4, 7.5, 'hello', True, s , b ]
l[4] = 'changed'
my_set = {1,2,3,3,3,5,'hello', 'hello'} # collection of unique members
print(my_set)
# dictionary
d = {'x':3, 'y':4} # a non-indexed mutable collection of key:value pairs