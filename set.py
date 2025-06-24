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