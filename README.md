# CorrectAnswer

'''

types of questions

a) just plain variables

ex1)
temp = 5
x = 7

ex2)
temp = 5
x = 8 + temp

temp = 5
x = temp + 8

ex3)
score = 8
score = score - 3

score = 8
score = 3 + score

ex4)
x = 3
y = 4
z = x - y

ex5)
x = 3
y = 4
z = x + 5

ex6)
x = 5
y = 4 - x
z = x + y - 3
a = z - 3 + y - 2 + x

ex7) 
x = 5
y = 4 - x
z = x + y - 3
x = z - 3 + y - 2 + x

b) if one variable

ex1)
y = 4
if y == 4:
    y = 8

ex2)
y = 4
if y != 4:
    y = 8

ex3)
y = 3
if y > 2:
    y = 5

c) if two variables

ex1)
flag = True
x = 6
if x > 10:
    flag = False

d) if else one variable

z = 4
if z == 2:
    z = 8
else:
    z = 5

e) if else two variables

x = 7
y = 3
if x > y:
    x = 6
else:
    y = 4

x = 7
y = 3
if x == y:
    x = 6 + y
else:
    y = 4 - x

f) if/elif/else 2-3 variable

x = 3
y = 4

if x == y:
    y = 6
elif x > y:
    x = 7
else: 
    z = 8

x = 3
y = 4
z = 5

if x == z:
    y = 6
elif y < 5:
    x = 7
else: 
    z = 8

g) if/if embedded 1 variables

x = 5
if x > 4:
    if x < 9:
        x = 6

h) if/if embedded 2 variable
x = 1
y = 2
if x == 0:
    if y == 2:
        x = 3

i) if/elif/if embedded 2 variables

ex1)
x = 2
y = 3
if x == y:
    if x == 3:
        x = 4
else:
    y = 5

ex2)
x = 2
y = 3
if x == y:
    if x == 3:
        y = 4
else:
    if y == 3:
        x = 7

ex3)
x = 2
y = 3
if x == y:
    if x == 3:
        y = 4
    else:
        x = 2
else:
    if y == 3:
        x = 7
    else:
        y = 7

ex4)
x = 2
y = 3
if x == y:
    if x == 3:
        y = 4
    else:
        x = 2
elif x < y:
    if y == 3:
        y = 5
    else:
        x = 3
else:
    if y == 3:
        x = 7
    else:
        y = 7

ex5)
x = 2
y = 3
if x == y:
    if x == 3:
        y = 4
    elif x < y:
        y = 7
    else:
        x = 2
elif x < y:
    if y == 3:
        y = 5
    elif x < y:
        y = 7
    else:
        x = 3
else:
    if y == 3:
        x = 7
    elif x < y:
        y = 7
    else:
        y = 7

j) if/AND/OR 2 variables
z = 7
y = 2
if z == 7 AND y == 2:
    z = 9

k) if/else/AND/OR 2 varaibles
z = 8
y = 2
if z == 7 OR y == 2:
    z = 9
else:
    y = 7

l) if/elif/else/AND/OR embedded 3 varaiables

z = 8
y = 2
x = 3
if z == 7 OR y == 2:
    if y == 3:
        x = 7
    elif x < y:
        y = 7
    else:
        y = 7
elif y == 2 AND z == 8:
    if y == 3:
        x = 7
    elif x < y:
        y = 7
    else:
        y = 7
else:
    if y == 3:
        x = 7
    elif x < y:
        y = 7
    else:
        y = 7

m) 

