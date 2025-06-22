# def my_function(fname):
#     print(fname + "Goodbye")

# my_function("Prajwal ")

# def my_function(fname, lname):
#     print(fname + " " + lname)

# my_function("Prajwal", "Nikhar")

# if you don't know how many arguments that will be passed into your 
# function, add a * before the parameter name in the function definition
# def my_function(*kids):

# print("The youngest kid is: " + kids[0])

# my_function("Arun", "Varun", "Karun")


# if you don't know how many keyword argument is unknown, add a dounle 
# ** before the parameter name
# def myFunction(**kid):
#     print("His last name is: " +kid["lname"])
# myFunction(fname = "Prajwal", lname = "Nikhar")

# Default parameter value
# def myFunction(country = "india"):
#     print("My country is: " + country)
# myFunction("England")
# myFunction("Australia")
# myFunction("America")

# Passing a list as an argument
# def my_func(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "orange"]
# my_func(fruits)

# # pass statement
# def myFunction():
#     pass

# Positional-only arguments
# def my_function(x, /):
#     print(x)
# my_function(3)

# def my_function(a, b, /, *, c, d):
#     print(a+b+c+d)
# my_function(5, 6, c=7, d=8)

# Recursion
def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("recursion example results: ")
tri_recursion(7)
