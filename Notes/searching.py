
# Searching (Chapter 15 from programarcadegames.com)

# Open a file to read
file = open('../data/super_villains.txt', 'r')    # open file to read

print(file)

for line in file:
    print("Hello", line.strip())    # you can only read through one time

file.close()    # ends your access to the file


# Open a file to write (overwrites all previous, no going back)
'''
file = open('../data/super_villains.txt', 'w')    # open file to write
file.write('Lee the Merciless\n')
file.close()

file = open('../data/super_villains.txt', 'r')    # open file to read

for line in file:
    print(line.strip())    # strip method removes ant extra spaces, \t, and \n

file.close()
'''

# Open a file to append (does not overwrite)
file = open('../data/super_villains.txt', 'a')
file.write('Dan the Man\n')
file.close()

file = open('../data/super_villains.txt', 'r')    # open file to read
print()
for line in file:
    print(line.strip())    # strip method removes ant extra spaces, \t, and \n

file.close()


# you can make a new file by opening to write
file = open('../data/oscars.txt', 'w')
file.write('Green Book\tBest Picture\n')
file.close()


# better way to open and close a file

with open('../data/super_villains.txt') as f:
    for line in f:
        print(line.strip())    # bog ol' string
    read_data = f.read()

# file automatically closes from with statement
print(read_data)


# Read data into a list (array)
with open('../data/super_villains.txt') as f:
    villains = [x.strip().upper() for x in f]

print(villains)





