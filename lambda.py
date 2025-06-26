# lambda
x = lambda a: a+10
print(x(5))

x = lambda a, b: a*b
print(x(2,3))

# function
def myfunc(n):
    return lambda a : a*n
my_doubler = myfunc(2)
print(my_doubler(23))

def myfunc1(n):
    return lambda a : a*n
mytripler = myfunc1(3)
print(mytripler(3))