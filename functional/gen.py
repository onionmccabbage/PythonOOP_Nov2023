# range, generators and comprehension
r = range(-100, 101, 3) # start, stop-before, step
# range is efficientt because it generates its values as needed
# so the values do not all exist in memory
# if we like, we CAN put all the values into memory
r_t = tuple(r) # the entire tuple exists in memory
r_l = list(r)
print(r_t, r_l)
# we can also make a generator object
v = (n**2 for n in range(-10, 11, 2))
print(v)
# we can iterate over a generator to comprehensively deal with every member
# this is called comprehension
print(v.__next__()) # 100

for item in v: # carry on the values
    print(item)

print(v.__next__()) # nope - the generator is exhausted
