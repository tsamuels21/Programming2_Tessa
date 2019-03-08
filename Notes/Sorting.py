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





