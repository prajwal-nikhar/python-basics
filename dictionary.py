
thisdict = {
	"car": "Volvo",
    "year": "2000",
    "Owner": "Raj",
    "Owner": "Prajwal",
    "color": ["red","yellow","blue"]
}
print(thisdict)
thisdict["number"] = "MH40KR9730"
print(thisdict)
print(thisdict.keys())
print(thisdict.values())
print(thisdict.get("year"))
print(thisdict["car"])

if "Owner" in thisdict:
	print("Yes, 'owner' is present in thisdict")
    
thisdict.update({"Owner": "Raj"})
thisdict.pop("color")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["car"]
print(thisdict)

thisdict.clear()
print(thisdict)

thisdict = {
	"car": "Volvo",
    "year": "2000",
    "Owner": "Raj",
    "Owner": "Prajwal",
    "color": ["red","yellow","blue"]
}

print(thisdict["year"])
print(thisdict["Owner"])
print(len(thisdict))
print(type(thisdict))

for x, y in thisdict.items():
	print(x, y)
    
# copy dictionary
my_dict = thisdict.copy()
print("my dict: ", my_dict)
#or
my_dict1 = dict(thisdict)
print("dict1: ", my_dict1)

thisdict = dict(name="John", age=27, city="LA")
print(thisdict.keys())
    