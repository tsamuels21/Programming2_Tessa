# PROBLEM 1 (Fibonacci)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.
import random

f = 1
s = 1

while f < 1001:
    print(f)
    print(s)
    f = (f + s)
    s = (f + s)


# PROBLEM 2 (Dice Sequence)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

# roll die
'''
prob = 0
h = 1000000

for i in range(h):
    roll_die = [random.randrange(1, 7) for x in range(5)]
    if roll_die[0] <= roll_die[1] and roll_die[1] <= roll_die[2] and roll_die[2] <= roll_die[3] and roll_die[3] <= roll_die[4]:
            prob += 1

probs = prob / h

print("The probability of success is: {:10}".format(probs))
'''

# PROBLEM 3 (Number Puzzler)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve. 

dcba = []
abcd = []









