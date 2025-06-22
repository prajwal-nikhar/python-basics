# Subscripting
print("Hello" [4])

# String
print("123" + "45")

#integer
print(123+456)

# Large Numbers/Integers
print(123_456 + 321_453)

# Float = Floating Point Number
print(123.45+34.6)

# Boolean
x=12
y=13
if x > y :
    print(x)
else :
    print(y)

# len() -> return the length of an object
len("Hello")


# type of datatype
print(type(10))
print(type(10.23))
print(type("String"))
print(type(True))

# typecasting
print(int("123") + int("234"))
print(int("123") + float("234.543"))
print(int(True) + int(False))


name_of_the_user = input("your name: ")
lenght_of_name = len(name_of_the_user)
print(type("Number of letters in your name:"))
print(type(lenght_of_name))
print("Number of letters in your name: " + str(lenght_of_name))


# PROJECT
# Tip Calculator
print("Welcome to the tip calculator: ",input("What is your name? "))

# bill
bill = float(input("What is total amount?\n$"))

# tip percentage
tip = int(input("How much tip you want to give? $10, $12, or $15:\n$"))

# total bill with tip
total_bill_with_tip = bill + tip

# splitting bill
total_person = int(input("Enter the number of persons you want to split the bill with:\n"))
bill_split = total_bill_with_tip/total_person

print(f"Each person should have to pay: ${bill_split}")
