list = ["apple", "banana", "kiwi", "orange", "cherry", "mango"]
newlist = []
for x in list:
    if 'a' in x:
        newlist.append(x)
print(newlist)

# extend list
l2 = [1,2,3,4,5]
newlist.extend(l2)
print(newlist)

# length of list
print(len(newlist))

# index
print(newlist[1])
print(newlist[1:3])
print(newlist[:4])
print(newlist[2:])

if 'apple' in newlist:
    print("YES 'apple' is present in newlist")
else:
    print("NO 'apple is not present in newlist")

# change item value
newlist[0] = "lichi"
print("change item value: ", newlist)

# change a range of item values
newlist[1:3] = ["guava", "watermelon"]
print("change a range of item values: ", newlist)

# insert items
newlist.insert(0, "cherry")
print(newlist)

# append
newlist.append("juice")
print("append: ", newlist)

# remove items
newlist.remove("juice")
print(newlist)

newlist.pop(0)
print(newlist)

newlist.pop()
print(newlist)

del newlist[2]
print(newlist)

# clear() list
newlist.clear()
print(newlist)

# delete entire list
del newlist