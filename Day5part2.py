# !/usr/bin/python3
# AdventOfCode2019 - Day5part2

data = input("Paste the input here and press [Enter]: ")
data = data.split(",")  # all inputs remain str now
index = 0


def add_leading_zero(x):
    return (5 - len(x)) * "0" + x


def interpret_command(x):
    opcode = x[3:5]
    mode1 = x[2]
    mode2 = x[1]
    mode3 = x[0]
    return [opcode, mode3 + mode1 + mode2]


def execute(modes, operator):
    global data
    global index
    global index_step

    if modes[1] == "0":
        a = int(data[int(data[index + 1])])
    else:
        a = int(data[index + 1])

    if modes[2] == "0":
        b = int(data[int(data[index + 2])])
    else:
        b = int(data[index + 2])

    if operator == "*":
        result = a * b
    elif operator == "+":
        result = a + b
    elif operator == "True":
        if a != 0:
            index = b
            index_step = 0
        else:
            index_step = 3
        return
    elif operator == "False":
        if a == 0:
            index = b
            index_step = 0
        else:
            index_step = 3
        return
    elif operator == "<":
        if a < b:
            result = 1
        else:
            result = 0
    elif operator == "=":
        if a == b:
            result = 1
        else:
            result = 0

    if modes[0] == "0":
        data[int(data[index + 3])] = str(result)
    else:
        data[index + 3] = str(result)


command = interpret_command(add_leading_zero(data[index]))
while int(command[0]) != 99:
    index_step = 4  # default
    if int(command[0]) == 1:  # addition
        execute(command[1], "+")
    elif int(command[0]) == 2:  # multiplication
        execute(command[1], "*")
    elif int(command[0]) == 3:  # input
        index_step = 2
        data[int(data[index + 1])] = input("Please provide your input:")
    elif int(command[0]) == 4:  # output
        index_step = 2
        print(data[int(data[index + 1])])
    elif int(command[0]) == 5:  # jump-if-true
        execute(command[1], "True")
    elif int(command[0]) == 6:  # jump-if-false
        execute(command[1], "False")
    elif int(command[0]) == 7:  # less than
        execute(command[1], "<")
    elif int(command[0]) == 8:  # equals
        execute(command[1], "=")
    index += index_step
    command = interpret_command(add_leading_zero(data[index]))
