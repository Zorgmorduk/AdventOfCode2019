# !/usr/bin/python3
# AdventOfCode2019 - Day5

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


def calculate(modes, operator):
    global data
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
    else:
        result = a + b
    if modes[0] == "0":
        data[int(data[index + 3])] = str(result)
    else:
        data[index + 3] = str(result)


command = interpret_command(add_leading_zero(data[index]))
while int(command[0]) != 99:
    index_step = 4
    if int(command[0]) == 1:  # addition
        calculate(command[1], "+")
    elif int(command[0]) == 2:  # multiplication
        calculate(command[1], "*")
    elif int(command[0]) == 3:  # input
        index_step = 2
        data[int(data[index + 1])] = input("Please provide your input:")
    elif int(command[0]) == 4:  # output
        index_step = 2
        print(data[int(data[index + 1])])
    index += index_step
    command = interpret_command(add_leading_zero(data[index]))
