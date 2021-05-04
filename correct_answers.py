import random
import sys
correct_answers = 0

keywords =  ['if', 'for', 'while']
variables = ['x', 'y', 'z', 'tmp', 'count']
math_operations = ['+', '-']
math_comparisions = ['<', '>', '==', '!=']
logic_operations = ['AND', 'OR', 'NOT']

#result = 0

def comp_new_values(count, var_list, math_op):
    new_values = []
    for _ in range(count):
        line = ''
        line += random.choice(var_list) + ' = ' + str(random.randint(0, 9)) 
        
        if(random.randint(0, 9) > 4):
            line += ' ' + random.choice(math_op) + ' ' + random.choice(var_list) + '\n'
        else:
            line += '\n'
        new_values.append(line)
    return new_values

def filter_branch_list(branch_list):
    if 'elif' in branch_list:
        if(random.randint(0, 9) > 3):
            branch_list.remove('elif')
    if 'else' in branch_list and 'elif' not in branch_list and random.randint(0, 9) > 3:
        branch_list.remove('else')
    return branch_list

def make_loop_condition(var_list, math_comp, logic_op):
    line = []
    var = 'flag'
    op = random.choice(math_comp)
    val = random.randint(0, 9)
    if(random.randint(0, 9) > 2):
        #variable
        line.append(var + ' ' + op + ' ' + str(val))
    else:
        #constant
        line.append(str(val) + ' ' + op + ' ' + var)

    if(op == '=='):
        line.append(var + ' = ' + str(val-1) + ' \n')
    elif(op == '!='):
        line.append(var + ' = ' + str(val)+ ' \n')
    elif(op == '<'):
        line.append(var + ' += 1'+ ' \n')
    elif(op == '>'):
        line.append(var + ' -= 1'+ ' \n')
    else:
        pass

    return line


def make_condition(var_list, math_comp, logic_op):
    line = ''
    if(random.randint(0, 9) > 2):
        #variable
        line += random.choice(var_list) + ' ' + random.choice(math_comp) + ' ' + str(random.randint(0, 9))
    else:
        #constant
        line += str(random.randint(0, 9)) + ' ' + random.choice(math_comp) + ' ' + random.choice(var_list)

    if(random.randint(0, 9) > 4):
        line += ' ' + random.choice(logic_op)
        if(random.randint(0, 9) > 2):
            #variable
            line += ' ' + random.choice(var_list) + ' ' + random.choice(math_comp) + ' ' + str(random.randint(0, 9))
        else:
            #constant
            line += ' ' + str(random.randint(0, 9)) + ' ' + random.choice(math_comp) + ' ' + random.choice(var_list)
    return line

def comp_if(branch_list, var_list, math_comp, logic_op):
    if_statements = []
    for keyword in branch_list:
        line = ''
        line += keyword + ' '
        if keyword == 'if' or keyword == 'elif':
            line += make_condition(var_list, math_comp, logic_op)
        line += ':\n'
        if_statements.append(line)
    return if_statements

def build_if(branch_list, var_list, math_comp, logic_op, math_op, indent, embed):
    branch_list = filter_branch_list(branch_list)
    new_values = comp_new_values(len(branch_list), var_list, math_op)
    if_statements = comp_if(branch_list, var_list, math_comp, logic_op)

    program = ''
    for index in range(len(branch_list)):
        program += ' ' *4*(indent-1) + if_statements[index]
        if(embed and random.randint(0, 9) < 2):
            program += build_if(branch_list, var_list, math_comp, logic_op, math_op, indent+1, False)
        else:
            program += ' ' *4*indent +new_values[index]
    return program

def create_problem(num_var=random.randint(2, 5), 
                   branch_list=['if','elif', 'else'], 
                   embed = True, 
                   math_op =  ['+', '-'], 
                   math_comp = ['<', '>', '==', '!='], 
                   logic_op =  ['and', 'or'], 
                   loop_list = []):
    program = ''
    var_list = []
    val_list = []
    
    #create values
    for _ in range(num_var):
        var_list.append(random.choice(variables))
        val_list.append(random.randint(0, 9))

    # initalize varaibles (can be duplicates)
    init_var = []
    for val in range(num_var):
        #print(var_list[val] + ' = ' + str(val_list[val]))
        #program += var_list[val] + ' = ' + str(val_list[val]) + '\n'
        init_var.append(var_list[val] + ' = ' + str(val_list[val]) + '\n')
    for line in init_var:
        program += line

    if loop_list != []:
        program += 'flag = ' + str(random.randint(0, 9)) + '\n'
        program += '\n'

    indent = 1
    loop_lines = []
    if loop_list != []:
        for loop in loop_list:
            line = ''
            line += loop + ' '
            loop_lines = make_loop_condition(var_list, math_comp, logic_op)
            line += loop_lines[0]
            line += ':\n'
            indent += 1
            program += line

    program += build_if(branch_list, var_list, math_comp, logic_op, math_op, indent, embed)

    program += '\n'

    if(random.randint(0, 9) > 2):
        program += build_if(branch_list, var_list, math_comp, logic_op, math_op, indent, False)

    if loop_lines != []:
        program += ' '*4 + loop_lines[1]

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

#num_var, branch_list, embed, math_op, math_comp, logic_op, loop_list)

result = create_problem()

for var, val in result:
    #print(var, val)
    answer = input('what is the value of ' + var + '?\n')
    while not answer.isnumeric():
        answer = input('what is the value of ' + var + '?\n')
    if(int(answer) == val):
        print('correct')
    else:
        print('inncorrect (ans: ' + str(val) + ')')


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