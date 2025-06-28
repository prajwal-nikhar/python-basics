cars = ["ford", "lamborgini", "Volvo", "BMW"]
print(cars[1])
x = len(cars)
# for loop
for x in cars:
    print(x)

# append
cars.append("toyota")
print(cars)

# pop
print(cars.pop())

# remove
cars.remove("Volvo")
print(cars)

# count
cnt = cars.count("BMW")
print(cnt)

# extend
fruits = ["apple", "banana", "orange"]
cars.extend(fruits)
print(cars)

# index
print(cars.index("BMW"))

# insert
cars.insert(2, "Volvo")
print(cars)

# reverse
cars.reverse()
print(cars)

# reverse sort
cars.sort(reverse=True)
print(cars)

# clear
cars.clear()
print(cars)