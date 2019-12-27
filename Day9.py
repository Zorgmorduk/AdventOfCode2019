# !/usr/bin/python3
# AdventOfCode2019 - Day9


def add_leading_zero(x):
    return (5 - len(x)) * "0" + x


def interpret_command(x):
    opcode = x[3:5]
    mode1 = x[2]
    mode2 = x[1]
    mode3 = x[0]
    return [opcode, mode1 + mode2 + mode3]


def execute(command, index, data, rel_base):
    index_step = 4  # default
    result = 0
    opcode = int(command[0])
    mode = command[1]

    if opcode == 3:  # input
        index_step = 2
        if mode[0] == "0":  # position mode
            data[int(data[index + 1])] = input("Please provide your additional input: ")
        elif mode[0] == "2":  # relative mode
            data[int(data[index + 1]) + rel_base] = input("Please provide your additional input: ")

    elif opcode == 4:  # output
        index_step = 2
        if mode[0] == "0":  # position mode
            print(data[int(data[index + 1])])
        elif mode[0] == "2":  # relative mode
            print(data[int(data[index + 1]) + rel_base])
    else:
        if mode[0] == "0":  # position mode
            a = int(data[int(data[index + 1])])
        elif mode[0] == "2":  # relative mode
            a = int(data[int(data[index + 1]) + rel_base])
        else:  # immediate mode
            a = int(data[index + 1])

        if mode[1] == "0":
            b = int(data[int(data[index + 2])])
        elif mode[1] == "2":  # relative mode
            b = int(data[int(data[index + 2]) + rel_base])
        else:
            b = int(data[index + 2])

        if opcode == 2:
            result = a * b
        elif opcode == 1:
            result = a + b
        elif opcode == 5:
            if a != 0:
                index = b
                index_step = 0
            else:
                index_step = 3
            return index, index_step, data, rel_base
        elif opcode == 6:
            if a == 0:
                index = b
                index_step = 0
            else:
                index_step = 3
            return index, index_step, data, rel_base
        elif opcode == 7:
            if a < b:
                result = 1
            else:
                result = 0
        elif opcode == 8:
            if a == b:
                result = 1
            else:
                result = 0
        elif opcode == 9:
            rel_base = rel_base + a
            index_step = 2
            return index, index_step, data, rel_base

        if mode[2] == "0":
            data[int(data[index + 3])] = str(result)
        elif mode[2] == "2":  # relative mode
            data[int(data[index + 3]) + rel_base] = str(result)
        else:
            data[index + 3] = str(result)

    return index, index_step, data, rel_base


def main():
    data = input("Paste the input here and press [Enter]: ")
    data = data + ",0" * 65536  # to extend the memory
    data = data.split(",")  # all inputs remain str now
    index = 0
    rel_base = 0
    command = interpret_command(add_leading_zero(data[index]))
    while int(command[0]) != 99:
        index, index_step, data, rel_base = execute(command, index, data, rel_base)
        index += index_step
        command = interpret_command(add_leading_zero(data[index]))


main()
