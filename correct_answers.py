
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



'''

import random

correct_answers = 0

keywords =  ['if', 'for', 'while']
variables = ['x', 'y', 'z', 'tmp', 'count', 'flag']
math_operations = ['+', '-']
math_comparisions = ['<', '>', '==', '!=']
logic_operations = ['AND', 'OR', 'NOT']

#result = 0

def create_problem(num_var, branch_list, embed, math_op, math_comp, logic_op):
    program = ''
    var_list = []
    val_list = []
    for _ in range(num_var):
        var_list.append(random.choice(variables))
        val_list.append(random.randint(0, 9))

    for val in range(num_var):
        #print(var_list[val] + ' = ' + str(val_list[val]))
        program += var_list[val] + ' = ' + str(val_list[val]) + '\n'

    if 'elif' in branch_list:
        if(random.randint(0, 9) > 3):
            branch_list.remove('elif')
    if 'else' in branch_list and 'elif' not in branch_list and random.randint(0, 9) > 3:
        branch_list.remove('else')

    for keyword in branch_list: 
        line = ''
        line += keyword 
        if keyword == 'if' or keyword == 'elif':
            if(random.randint(0, 9) > 2):
                #variable
                line += ' ' + random.choice(var_list) + ' ' + random.choice(math_comp) + ' ' + str(random.randint(0, 9))
            else:
                #constant
                line += ' ' + str(random.randint(0, 9)) + ' ' + random.choice(math_comp) + ' ' + random.choice(var_list)

            if(random.randint(0, 9) > 4):
                line += ' ' + random.choice(logic_op)
                if(random.randint(0, 9) > 2):
                    #variable
                    line += ' ' + random.choice(var_list) + ' ' + random.choice(math_comp) + ' ' + str(random.randint(0, 9))
                else:
                    #constant
                    line += ' ' + str(random.randint(0, 9)) + ' ' + random.choice(math_comp) + ' ' + random.choice(var_list)
            
        line += ':'
        #print(line)
        program += line + '\n'
        #print('    ' + random.choice(var_list) + ' = ' + str(random.randint(0, 9)))
        program += '    ' + random.choice(var_list) + ' = ' + str(random.randint(0, 9)) 
        
        if(random.randint(0, 9) > 4):
            program += ' ' + random.choice(math_op) + ' ' + random.choice(var_list) + '\n'
        else:
            program += '\n'

    line = 'print('
    line_1 = 'result = {'

    for var in set(var_list):
        line += var + ', '
        line_1 += "('" + var +"', " + var + ')'+ ', '

    line = line[:-2] + ')'
    line_1 = line_1[:-2] + '}'

    #program += line + '\n'
    print(program)

    program += 'global result\n'
    program += line_1 + '\n'

    #print(line)
    #print(program)
    global result
    exec(program)

    return result




result = create_problem(random.randint(2, 5), ['if','elif', 'else'], False, ['+', '-'], ['<', '>', '==', '!='], ['and', 'or'])
'''
for var, val in result:
    #print(var, val)
    answer = input('what is the value of ' + var + '?\n')
    if(int(answer) == val):
        print('correct')
    else:
        print('inncorrect (ans: ' + str(val) + ')')
'''

'''
#level one just two variables
while correct_answers < 2:
    #keyword = random.choice(keywords)
    var1 = random.choice(variables)
    var2 = random.choice(variables)

    val1 = random.randint(0, 9)
    val2 = random.randint(0, 9)

    print(var1 + ' = ' + str(val1))
    print(var2 + ' = ' + str(val2))
    print()

    if(var1 == var2):
        ans1 = int(input('what is the value of ' + var1 + ': '))
        if ans1 == val2:
            print("that's right! you get a point")
            correct_answers += 1
        else:
            print("that's not right")
    else:
        ans1 = int(input('what is the value of ' + var1 + ': '))
        ans2 = int(input('what is the value of ' + var2 + ': '))
        print()
            

        if(ans1 == val1 and ans2 == val2):
            print("that's right! you get a point")
            correct_answers += 1
        else:
            print("that's not right")
    print('score: ' + str(correct_answers))
    print("let's try again")
    print()

while correct_answers < 4:
    #keyword = random.choice(keywords)
    var1 = random.choice(variables)
    var2 = random.choice(variables)

    val1 = random.randint(0, 9)
    val2 = random.randint(0, 9)

    math_op = random.choice(math_operations)

    print(var1 + ' = ' + str(val1))
    print(var2 + ' = ' + str(val2) + ' ' + math_op + ' ' + var1)
    print()

    ans1 = int(input('what is the value of ' + var2 + ': '))

    if(math_op == '+'):
        sol1 = val2 + val1    
    elif(math_op == '-'):
        sol1 = val2 - val1

    if(ans1 == sol1):
        print("that's right! you get a point")
        correct_answers += 1
    else:
        print("that's not right")
    print('score: ' + str(correct_answers))
    print("let's try again")
    print()

print('great job!')
'''
'''
while correct_answers < 4:
    #keyword = random.choice(keywords)
    var1 = random.choice(variables)
    var2 = random.choice(variables)

    val1 = random.randint(0, 9)
    val2 = random.randint(0, 9)

    math_op = random.choice(operations)
'''