'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''
import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open('dictionary.txt')
dictionary_list = []

for line in file:
    line = line.strip()
    words = split_line(line)
    for word in words:
        dictionary_list.append(word)
file.close()


print("--- Linear Search ---")

file = open("AliceInWonderLand200.txt")
line_number = 0

for line in file:
    line = line.strip()
    line_number += 1
    words = split_line(line)
    for word in words:
        i = 0
        while i < (len(dictionary_list)) and word.upper() != dictionary_list[i]:
            i += 1
        if i > len(dictionary_list) -1:
            print("Line", line_number, " possible misspelled word:", word)

file.close()


print("--- Binary Search ---")

file = open("AliceInWonderLand200.txt")
line_number = 0

for line in file:
    line = line.strip()
    line_number += 1
    words = split_line(line)
    for word in words:
        lower = 0
        upper = len(dictionary_list)
        found = False
        key = word.upper()

        while lower <= upper and not found:
            middle_pos = (upper + lower) // 2
            if dictionary_list[middle_pos] < key:
                lower = middle_pos + 1
            elif dictionary_list[middle_pos] > key:
                upper = middle_pos - 1
            else:
                found = True

        if not found:
            print("Line", line_number, "Possible incorrect spelling:", word)

file.close()




