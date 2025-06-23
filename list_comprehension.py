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
<<<<<<< HEAD
del newlist
=======
del newlist

# sorting list
l3 = [1,23,3,12,443,234,10,9,4]
l3.sort()
print(l3)

l3.sort(reverse=True)
print(l3)
# or
l3.reverse()
print("reverse sort:", l3)

# customize sort function
def my_function(k):
    return abs(k - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=my_function)
print(thislist)

# case insensitive sort
thislist1 = ["banana", "kiwi", "Orange", "Apple"]
thislist1.sort(key=str.lower)
print(thislist1)

# joining two list
l1 = ["a", "b", "c", "d"]
l4 = [1,2,3,3,3,3,1]
for x in l1:
    l4.append(x)
print(l4)

# count
x = l4.count(3)
print(x)

'''
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
'''

for i in l4:
    count = l4.count(3)
    if count != 0:
        l4.remove(3)
    else: 
        break
print(l4)

# or
l4 = [x for x in l4 if x!=3]
print(l4)
>>>>>>> e09a84b (list)
