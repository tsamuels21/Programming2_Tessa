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

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print("The longest word is ", longest_word('dictionary.txt'))


print()
#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

length_list = []

file = open('AliceInWonderLand.txt')
num = 0
avg = 0
for line in file:
    line = line.strip()
    words = split_line(line)
    for letter in words:
        num += 1
        let = len(letter)
        length_list.append(let)

sum = sum(length_list)
print("The average word is {:.1f}".format(sum / num), "letters long")
print("The total word count is", num, "words")

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS
print()
#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####
file = open('AliceInWonderLand.txt')
alice = []

for line in file:
    line = line.strip()
    words = split_line(line)
    for word in words:
        alice.append(word)

seven_w = []
for i in alice:
    if len(i) == 7:
        seven_w.append(i)
seven = []
for i in seven_w:
    seven.append(seven_w.count(i))

most = seven_w[seven.index(max(seven))]
print("The most frequently occurring 7 letter word is ", most)


#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



