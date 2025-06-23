thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print(type(thistuple))

# NOT a tuple: To create a tuple with only one item, you have to add a 
# comma after the item otherwise python will not recognize it as a 
# tuple
thistuple = ("apple")
print(type(thistuple))

# Access tuple items
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
# negative indexing
print(thistuple[-1])
print(thistuple[-4:-1])
# Range of indexes
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

# update tuple
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)

y.append("orange")
thistuple = tuple(y)
print(thistuple)

print(y)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# for loop
for x in thistuple:
    print(x)
# or
for i in range(len(thistuple)):
    print(thistuple[i])

# while loop
i=0
while i<len(thistuple):
    print("while loop: ", thistuple[i])
    i = i + 1

del thistuple
print(thistuple)

# methods in tuple
'''
1. count()
2. index()
'''