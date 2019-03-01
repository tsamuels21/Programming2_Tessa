'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

letters_list = []

file = open('dictionary.txt')

for line in file:
    line = line.strip()
    words = split_line(line)
    for letter in words:
        let = len(letter)
        letters_list.append(let)

print(letters_list)



print()
#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

letters_list = []

file = open('AliceInWonderLand.txt')
num = 0

for line in file:
    line = line.strip()
    words = split_line(line)
    for letter in words:
        let = len(letter)
        letters_list.append(let)



print(letters_list)
print(num)

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####

#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



