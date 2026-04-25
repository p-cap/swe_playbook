import random

# my_array = [random.randint(1,99) for i in range(10)]
# print(my_array)
my_array = [64, 17, 82, 18, 82, 7, 56, 85, 51, 15]

# in place sort
# my_array.sort()
# print(my_array)

my_array_two = [21, 87, 53, 16, 21, 43, 93, 5, 97, 32]
# print(my_array_two)
# sorted() returns a new array
my_array_two = sorted(my_array_two)
print(my_array_two)
my_array_two.reverse()
print(my_array_two)
print('--- reversing my_array ---')
print(my_array)
print(my_array[::-1])
"""arr.insert(i, x)`
my_array = [i for i in range(1,11)]
my_array.insert(2,999999)
print(my_array)
"""
