#Lambda Fubctions

lambda num : num * 2

multiply = lambda a, b : a * b

print(multiply(2,54))

#Map, Filter, Reduce 

numbers = [1,2,3,4]

double = lambda a : a * 2 #a is an item in the list

result = map(double, numbers)

print(list(result))

numbers_filter = [1,2,3,4,5,6,7,8,9]

def isEven(n):
    return n % 2 == 0
#result_filter = filter(isEven, numbers_filter)

result_filter = lambda x : x % 2 == 0

result_filter = filter(result_filter, numbers_filter)

print(list(result_filter))

#Reduce 
from functools import reduce

dinner = [('Pizza', 45), ('Juice', 12)]

sum = reduce(lambda a, b: a[1] + b[1], dinner)

print(sum)


from functools import reduce

expenses = [
    ('Dinner', 80), ('Car repair', 120),
            ('Books', 12), ('Lunch', 34)
            ]

sum = reduce(lambda a, b: a + b[1], expenses, 0)

print(sum)

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
squares = []

for x in a:
    squares.append(x**2)
print(squares)

alt = map(lambda x: x**2, filter(lambda x: x % 2 ==0, a))

print(list(alt))


#Recursion

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(5))

#Decorators

#Allows you to modify or extend the behavior of functions or methods without changing their actual code

def logtime(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    return wrapper

@logtime
def hello():
    print('Hello')
    
hello()

#List Compression

#Make it simple instead of couple of lines 

number = [1,2,3,4,5,6,7,8]

number_power_2 = [n**2 for n in number]
print(number_power_2)
