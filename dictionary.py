#to add a key to a dictionary.
'''d= {0:10, 1:20, 3:40}

print(d)

d.update({2:30})
print(d)'''


#concatenate the following dictionaries to create a new one.

'''dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
dict4 = {}
for i in (dict1, dict2, dict3):
    print(i)
    dict4.update(i)
print(dict4)'''

#whether a given key already exists in a dictionary.

'''d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print("Key present in the dictionary")
    else:
        print("Key is not present in the dictionary")


is_key_present(5)
is_key_present(7)'''

#program to iterate over dictionaries using for loops.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#d2 = {1: 10, 2: 20, 3: 30}
#d1= {}

'''for k, v in d.items():
    print(k, "->", v)'''


'''for i in (d,):
    print(i)'''


#print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input("Input a number"))
d= {}

for x in range(1, n+1):
    print(x)
    d[x] = x**x

print(d)


# the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

'''d={}

for i in range(1, 16):
    print(i)
    d[i] = i*i

print(d)'''


# merge two Python dictionaries.

'''d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
d2 = {5:50, 6:60}

d = {}

for i in(d1,d2):
    #print(i)
    d.update(i)
print(d)'''

# iterate over dictionaries using for loops.

'''d= {1: 1, 2: 4, 3: 9, 4: 16, 5: 50, 6: 60}

for k, v in d.items():
    print(k," corresponds to",v)'''


# sum all the items in a dictionary.

'''d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 50, 6: 60}
print(sum(d.values()))'''


# sort a given dictionary by key


'''d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 50, 6: 60}
print(sorted(d.keys()))'''


# the maximum and minimum values of a dictionary.
'''d = {'x':500, 'y':5874, 'z': 560}

print(max(d.values()))
print(min(d.values()))'''


# get a dictionary from an object's fields.

'''class dictObj(object):
    def __init__(self):
        self.x = "red"
        self.y = "Yellow"
        self.z = "Green"
    def do_nothing(self):
        pass

test = dictObj()
print(test.__dict__)'''


# match key values in two dictionaries

'''d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}

for k,v in set(d1.items()) & set(d2.items()):
    print(k,v)'''

# display version
    
'''import sys
print("Python version")
print(sys.version) 

print("Python version_info")
print(sys.version_info)'''

# display current date and time

'''import datetime
now = datetime.datetime.now()

print(now)'''


