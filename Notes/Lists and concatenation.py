'''
my_list = []
my_list.revers()    # reverses the order
print(my_list)

# import one!   pop method
my_list.pop()   # pops one off the end of the list
print(my_list)
customer = my_list.pop()    # pops and returns which one you want to grab

# concatenation
first = "Francis"
last = "Parker"
print(first + last)

print(my_list + my_numbers)
'''


# ITERATING THOUGH LISTS
# make a lst of numbers 0 to 9
import random

my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)

print()

# print every item in my_list
# for each loop (uses a copy of each item)
for number in my_list:
    number += 1
    print(number)
print(my_list)

print()

# index variable loop
for i in range(len(my_list)):
    my_list[i] += 1
    print(my_list[i])
print(my_list)

print()

# make a 2d list that is 10 x 10 [[0, 0], [0, 1], [0, 2], [0, 3]... [9, 9]]
my_list = []
for i in range(10):
    for j in range(10):
        my_list.append([i, j])
print(my_list)

# print each pair
for pair in my_list:
    print(pair)

# print each i value
for pair in my_list:
    print(pair[0])

print()

# LIST COMPREHENSIONS   (show old way then the new way)
# [returned_item for iterator in list/range filter]
# Syntactic Sugar

# make a list from 0 to 100
my_list = []
for i in range(101):
    my_list.append(i)
print(my_list)

my_list = [x for x in range(101)]
print(my_list)

print()

# make a list of 0 to 100 squared
my_list = []
for i in range(101):
    my_list.append(i ** 2)
print(my_list)

my_list = [x ** 2 for x in range(101)]
print(my_list)

print()

# make a list 0 to 100 squared, but filter out the odd numbers
my_list = []
for i in range(101):
    if i ** 2 % 2 == 0:
        my_list.append(i ** 2)
print(my_list)

my_list = [x ** 2 for x in range(101) if x ** 2 % 2 == 0]
print(my_list)

print()

# roll a single die 100 times and add it to a list
my_list =[]
for i in range(100):
    my_list.append(random.randrange(1, 7))
print(my_list)

my_list = [random.randrange(1, 7) for x in range(100)]
print(my_list)

print()

# roll 2 die 100 times and add it to a list
my_list = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]
print(my_list)

print()

# roll 2 die 100 times, only show the doubles
my_list = [x for x in my_list if x[0] == x[1]]
print(my_list)

print()

# all at once
my_list = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)] if x[0] == x[1]]
print(my_list)


# Working wih strings
first = "Francis"
last = "Parker"
print(first[0])
first = first.upper()
print(first)
print(first + last)
print(last[-2:])
if "F" in first:
    print("Yep")

for char in last:
    print(char)

word_bank = ["TIGER", "SEAL", "MONKEY"]

my_word = word_bank.pop(random.randrange(len(word_bank)))
print(my_word)


