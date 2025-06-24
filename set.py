myset = {"apple", "banana", "cherry", "apple"} # set cannot have two items with the same value
print(myset)

thisset = {"apple", "banana", "cherry", True, 1, 2} #True and 1 is considered as the same value
print(thisset)

print(len(thisset))
print(type(thisset))

# set() constructor
thisset1 = set(("apple", "banana", "cherry")) # double round brackets
print(thisset1)

# for loop
for x in thisset:
    print(x)

print("banana" not in thisset)
# once a set is created, you cannot change its items, but you can add new items

thisset.add("orange")
print(thisset)
tropical = {"kiwi", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# add elements of a list to at set:
list = ["lichi", "guava"]
thisset.update(list)
print(thisset)

# remove, discard(), pop(), clear(), del
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)
thisset.pop()
print(thisset)

# thisset.clear()
# print(thisset)

# del thisset
# print(thisset) -> as we have deleted the set now it will give an error

# loop items
for x in thisset:
    print(x)

# join sets
# union(), update(), intersection(), difference(), symmetric_difference()
set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3, 4}
set3 = set1.union(set2)
print(set3)
# or
set3 = set2 | set1
print(set3)

# multiple sets
# union
set4 = {"Sumit", "Sayandip"}
set5 = {"apple", "banana", "orange"}
set6 = set1.union(set2, set3, set4, set5)
print(set6)
# 
myset = set1 | set2 | set3 | set4 | set5
print(myset)

# join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1.update(set2)
print(set1)

# intersection
set11 = {"apple", "banana", "cherry"}
set21 = {"google", "microsoft", "apple"}
set31 = set11.intersection(set21)
print(set31)
# or
set32 = set11 & set21
print(set32)

# intersection update
set11.intersection_update(set21)
print(set11)

set111 = {"apple", 1,  "banana", 0, "cherry"}
set211 = {False, "google", 1, "apple", 2, True}
set311 = set1.intersection(set211)
print(set311)

# difference
set322 = set1.difference(set2)
print(set322)
# or
set333 = set1 - set2
print(set333)

# difference update
set1.difference_update(set2)
print(set1)

# symmetric difference
sets = set1.symmetric_difference(set2)
print(sets)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# symmetric difference update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)