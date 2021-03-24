import os

clear = lambda: os.system("cls")
clear()

remainder = lambda num: num % 2

print(remainder(5))

product = lambda x, y: x * y

print(product(2, 3))


def testfunc(num):
    return lambda x: x * num


result1 = testfunc(10)
result2 = testfunc(1000)
print(result1(9))
print(result2(9))

numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
new = [num for num in numbers_list if num > 7]
print(new)

filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)


def addition(n):
    return n + n


# we double all numbers using regular function
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

result3 = map(lambda num: num + num, numbers)
print(list(result3))


# Two arguments
numbers = (1, 2, 3, 4)
numbers2 = (5, 6, 7, 8)
result3 = map(lambda x, y: x + y, numbers, numbers2)
print(list(result3))