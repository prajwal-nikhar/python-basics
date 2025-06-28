class Person:
    def  __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self, name, age):
        self.name = name
        self.age = age
    
    def my_func(self):
        print("Hello, my name is " + self.name)

    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("John", 36)
p1.my_func()
p1.myfunc()
print(p1.name)
print(p1.age)

p2 = Person("Prajwal", 25)
print(p2.name)
print(p2.age)    

# modify property object
p1.age = 40
print(p1.age)

# del object properties
del p1.age
# print(p1.age)

# delete objects
del p1
# print(p1)

# the pass statement
class Man:
    pass

