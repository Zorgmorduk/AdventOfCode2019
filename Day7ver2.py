# !/usr/bin/python3
# AdventOfCode2019 - Day7ver2

from itertools import permutations


def add_leading_zero(x):
    return (5 - len(x)) * "0" + x


def interpret_command(x):
    opcode = x[3:5]
    mode1 = x[2]
    mode2 = x[1]
    mode3 = x[0]
    return [opcode, mode1 + mode2 + mode3]


def execute(command, index, data, phase, signal, second_run):
    index_step = 4  # default
    result = 0
    output = None
    opcode = int(command[0])
    mode = command[1]

    if opcode == 3:  # input
        index_step = 2
        if second_run:
            data[int(data[index + 1])] = signal
        else:
            data[int(data[index + 1])] = phase
            second_run = True
    elif opcode == 4:  # output
        index_step = 2
        print(data[int(data[index + 1])])
        output = data[int(data[index + 1])]
    else:
        if mode[0] == "0":
            a = int(data[int(data[index + 1])])
        else:
            a = int(data[index + 1])

        if mode[1] == "0":
            b = int(data[int(data[index + 2])])
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
            return index, index_step, data, output, second_run
        elif opcode == 6:
            if a == 0:
                index = b
                index_step = 0
            else:
                index_step = 3
            return index, index_step, data, output, second_run
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

        if mode[2] == "0":
            data[int(data[index + 3])] = str(result)
        else:
            data[index + 3] = str(result)

    return index, index_step, data, output, second_run


def intcode(data, phase, signal):
    index = 0
    output = None
    second_run = False
    command = interpret_command(add_leading_zero(data[index]))
    while int(command[0]) != 99:
        index, index_step, data, output, second_run = execute(command, index, data, phase, signal, second_run)
        index += index_step
        command = interpret_command(add_leading_zero(data[index]))
    return output


def main():
    data = input("Paste the input here and press [Enter]: ")
    data = data.split(",")  # all inputs remain str now
    results = []

    perm = permutations([0, 1, 2, 3, 4])
    for sequence in perm:
        outputA = intcode(data, sequence[0], 0)
        outputB = intcode(data, sequence[1], outputA)
        outputC = intcode(data, sequence[2], outputB)
        outputD = intcode(data, sequence[3], outputC)
        outputE = intcode(data, sequence[4], outputD)
        results.append(int(outputE))

    print("The answer is:", max(results))


main()
