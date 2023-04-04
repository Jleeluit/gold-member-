import random

var = {}

print(var)

print(type(var))

var2 = {"number":386}

print(var2)

var2["fruit"] = "apple"

print(var2)

var2["number"] = 493

print(var2)

print(dir(var))

print(list(var2.keys()))
print(list(var2.values()))

for k, v in var2.items():
    print(k, v)
    
### dont look at this code

dict_of_lists = {i:[random.randint(0,10) for j in range(5)] for i in range(5)} # dict comprehension

### you can look again

for k, v in dict_of_lists.items():
    print(k, v)
    for element in v:
        print(element)