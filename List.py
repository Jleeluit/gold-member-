import random

var = []

print(type(var))

var2 = [251, 386, 493]

print(var2)

var3 = [251, 386, 493, "009"]

var3.append(649) # inplace function
var3 = var3 + [721] # not inplace

print(var3)

#print(dir(var3))

var3.reverse()

print(var3)

numbers = [1,2,3,4,5]

print(numbers)

r = range(0,20)

print(r)

print(list(r))

for number in numbers:
    print(number*2)
    
for i in range(10):
    print(i)
    
print(var3)
print(var3[1])

print(len(var3))

for i in range(len(var3)):
    print(var3[i])
    
### dont look at this code

list_of_lists = [[random.randint(0,10) for j in range(5)] for i in range(5)] # list comprehension

### you can look again

print(list_of_lists)

for l in list_of_lists: # didnt use the variable name list because its a keyword
    print(l)
    for element in l:
        print(element)
        
for i in range(len(list_of_lists)): # didnt use the variable name list because its a keyword
    print(list_of_lists[i])
    for j in range(len(list_of_lists[i])):
        print(list_of_lists[i][j])