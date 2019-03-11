# Sorting

# Swap values
import random

a = 1
b = 2
print(a, b)

temp = a    # temporarily store on value before i overwrite it
a = b
b = temp
print(a, b)


# pythonic way
a, b = b, a    # one line swap
print(a, b)


# Selection Sort

# make a random list of 100 numbers from 1 to 99
rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)

for cur_pos in range(len(rand_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(rand_list)):
        if rand_list[scan_pos] < rand_list[min_pos]:
            min_pos = scan_pos
    rand_list[min_pos], rand_list[cur_pos] = rand_list[cur_pos], rand_list[min_pos]    # commit the change

print("Selection Sort")
print(rand_list)

print()
# Insertion Sort

rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)

for key_pos in range(1, len(rand_list)):
    key_val = rand_list[key_pos]    # store the value
    scan_pos = key_pos - 1    # look to the left
    while (scan_pos >= 0) and (rand_list[scan_pos] > key_val):
        rand_list[scan_pos + 1] = rand_list[scan_pos]
        scan_pos -= 1

    # everything had shifted to make room for key_value
    rand_list[scan_pos + 1] = key_val

print(rand_list)

print()
# Sorting in real life with Python
rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)

# sort method (sorts in place; changes list directly)
rand_list.sort()
print(rand_list)

print()
# sorted function (returns a sorted list)
rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)

rand_list2 = sorted(rand_list)  # capture the returned list
print(rand_list2)

print()
# optional parameters
print("Hello", end="")  # end="" is an optional parameter that has a default value of "\"
print("World")

def hello(name, time="8:43"):
    print("Good Morning Mr. Stark", name, "it is now", time, "am")

hello("Mr. Stark", time="8:44")

print()
# Lambda Function (anonymous function on a single line)
double_me = lambda x: 2 * x    # lambda parameter: return
print(double_me(10))

print()
# Sorted function using a lambda function
# optional key parameter is what you are using to sort the list
my_list = ["Abel", "evan", "Zed", "Piper", "len", "Jenny", "Kip"]
my_sort = sorted(my_list, key=lambda x: x.upper())
print(my_sort)

my_list.append("Alex")
my_sort = sorted(my_list, key=lambda x: len(x))
print(my_sort)

my_list = [["Abel", 8], ["evan", 10], ["Zed", 11], ["Piper", 17], ["len", 16], ["Jenny", 28], ["Kip", 80]]
my_sort = sorted(my_list, key=lambda x: x[1])
print(my_sort)

