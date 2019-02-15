# Formatting
import random
# Floating point error
x = 2 / 3 - 1 + 1 / 3   # this should be 0
if x == 0:
    print(x)

# round
x = 8 / 3
print(x)
print(int(x))
print(x // 1)
print(round(x))

x = 235236.2957864
print(round(x, 2))
print(round(x, 0))
print(round(x, -1))


# format method is more useful
#  index:spaceholder+justification+sign+width+commas+precision+datatype+notation

x = 784265105634
y = 3.4
print("x is: {}\ty is: {}".format(x, y))    # more than 1 item
print("y is: {1}\tx is: {0}".format(x, y))    # using indices

# width (number of spaces)
print("x is: {:10}".format(x))

# spaceholder
print("x is: {:015}".format(x))    # 0 is the spaceholder

# justification (<, >, ^)
print("x is: {:>10} units".format(x))    # right justify

# sign (+, -) and comma (, if you want em)
for i in range(20):
    x = random.randrange(-1000000, 1000000)
    print("x is {:>+8,}".format(x))  # force positive and negative signs

# precision (.2f would be 2 decimals floating point)
# datatype (could be f(loat), b(inary), x(hex), d(ecimel), e(xponent) or int), %,
for i in range(20):
    x = random.random() * 200 - 100
    print("x is: {:.5f}".format(x))

for i in range(20):
    x = random.randrange(256)
    print("x in binary is: {:9b}".format(x))

x = random.randrange(256)
print("x in hex is: {:9x}".format(x))

