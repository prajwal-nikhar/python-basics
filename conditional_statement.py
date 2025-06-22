print("Welcome to the rollercoaster ride")

height = int(input("What is your height: "))

if height > 120:
    print("You can ride on rollercoaster ride")
else:
    print("Sorry you cannot ride on rollercoaster ride")

number_to_check = int(input("what is the number you want to check?\n"))
# divisor = int(input("Enter divisor:\n"))

if number_to_check%2 == 0:
    print("Number is even")
else:
    print("number is odd")