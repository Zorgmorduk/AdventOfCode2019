# !/usr/bin/python3
# AdventOfCode2019 - Day5part2ver2


def add_leading_zero(x):
    return (5 - len(x)) * "0" + x


def interpret_command(x):
    opcode = x[3:5]
    mode1 = x[2]
    mode2 = x[1]
    mode3 = x[0]
    return [opcode, mode1 + mode2 + mode3]


def execute(command, index, data):

    index_step = 4  # default
    operator = int(command[0])
    mode = command[1]

    if operator == 3:  # input
        index_step = 2
        data[int(data[index + 1])] = input("Please provide your additional input: ")
    elif operator == 4:  # output
        index_step = 2
        print(data[int(data[index + 1])])
    else:
        if mode[0] == "0":
            a = int(data[int(data[index + 1])])
        else:
            a = int(data[index + 1])

        if mode[1] == "0":
            b = int(data[int(data[index + 2])])
        else:
            b = int(data[index + 2])

        if operator == 2:
            result = a * b
        elif operator == 1:
            result = a + b
        elif operator == 5:
            if a != 0:
                index = b
                index_step = 0
            else:
                index_step = 3
            return index, index_step, data
        elif operator == 6:
            if a == 0:
                index = b
                index_step = 0
            else:
                index_step = 3
            return index, index_step, data
        elif operator == 7:
            if a < b:
                result = 1
            else:
                result = 0
        elif operator == 8:
            if a == b:
                result = 1
            else:
                result = 0

        if mode[2] == "0":
            data[int(data[index + 3])] = str(result)
        else:
            data[index + 3] = str(result)

    return index, index_step, data


def main():
    data = input("Paste the input here and press [Enter]: ")
    data = data.split(",")  # all inputs remain str now
    index = 0
    command = interpret_command(add_leading_zero(data[index]))
    while int(command[0]) != 99:
        index, index_step, data = execute(command, index, data)
        index += index_step
        command = interpret_command(add_leading_zero(data[index]))


main()
