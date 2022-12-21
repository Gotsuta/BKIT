#list of tuples (value, square of value)

a = [1,2,3]
########## 1 ##########
b = ()
c = []
for i in a:
    list(b).append((i, i**2))
    c.append((i, i**2))

print(c)
########################

########## 2 ##########

print(list(map(lambda x: (x, x**2), a)))

########################

########## 3 ##########
print(list(zip(a, map(lambda x: x**2, a))))

############ 4 #########
com = [(i, i**2) for i in a]
print(com)
########################