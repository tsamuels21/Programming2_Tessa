'''
FORMATTING PROBLEM SET (12 PTS)
'''
# Tessa
# put your name HERE
# https://github.com/fwparkercode/Programming2_SP19
# New change

'''
PROBLEM 1 (2pts)
Use {}.format() to print 0.000321192 in scientific notation to two decimals
'''

x = 0.000321192

print("x in scientific notation is {:.2e}".format(x))

print()
'''
PROBLEM 2 (2pts)
You get 8 out of 9 on a quiz.
Print 8/9 using {}.format() so that it appears as 89%
'''

score = 8 / 9
print("Your score is {:.0%}".format(score))

print()
'''
PROBLEM 3 (3pts)
Take the following program:

score = 41237
highscore = 1023407
print("Score:      " + str(score) )
print("High score: " + str(highscore) )

Which right now outputs:
Score:      41237
High score: 1023407

Use print formatting so that the output instead looks like:
Score:          41,237
High score:  1,023,407

Make sure the print formatting works for any integer from zero to nine million. 
Do not use any concatenation in your code (no plus signs). 
You should only have two double quotes in each print statement.
'''

score = 41237
highscore = 1023407

print("Score: " "{:14,}".format(score))
print("High Score: " "{:7,}".format(highscore))


print()
'''
PROBLEM 4 (5 pts) 
Create a program that loops from 1 to 20 and lists the decimal equivalent of their inverse. 
Use print formatting to EXACTLY match the following output:
1/1  = 1.0
1/2  = 0.5
1/3  = 0.333
1/4  = 0.25
1/5  = 0.2
1/6  = 0.167
1/7  = 0.143
1/8  = 0.125
1/9  = 0.111
1/10 = 0.1
1/11 = 0.0909
1/12 = 0.0833
1/13 = 0.0769
1/14 = 0.0714
1/15 = 0.0667
1/16 = 0.0625
1/17 = 0.0588
1/18 = 0.0556
1/19 = 0.0526
1/20 = 0.05
'''
'''
for i in range(1, 21):
    x = 1 / i
    if i < 10:
        print("1/"+ str(i), " = {:.3}".format(x))
    if i >= 10:
        print("1/"+ str(i), "= {:.3}".format(x))
'''




