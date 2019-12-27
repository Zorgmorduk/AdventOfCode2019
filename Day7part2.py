# !/usr/bin/python3
# AdventOfCode2019 - Day7part2

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


def intcode(data, index, second_run, phase, signal):
    output = None
    command = interpret_command(add_leading_zero(data[index]))
    opcode = int(command[0])
    while opcode != 99 and output is None:
        index, index_step, data, output, second_run = execute(command, index, data, phase, signal, second_run)
        index += index_step
        command = interpret_command(add_leading_zero(data[index]))
        opcode = int(command[0])
    return opcode, output, data, index, second_run


def main():
    data = input("Paste the input here and press [Enter]: ")
    data = data.split(",")  # all inputs remain str now
    results = []

    perm = permutations([5, 6, 7, 8, 9])
    for sequence in perm:
        dataA, dataB, dataC, dataD, dataE = data.copy(), data.copy(), data.copy(), data.copy(), data.copy()
        indexA, indexB, indexC, indexD, indexE = 0, 0, 0, 0, 0
        second_runA, second_runB, second_runC, second_runD, second_runE = False, False, False, False, False
        cont = True
        first_run = True
        while cont:
            if first_run:
                outputE = 0
                first_run = False
            opcodeA, outputA, dataA, indexA, second_runA = intcode(dataA, indexA, second_runA, sequence[0], outputE)
            opcodeB, outputB, dataB, indexB, second_runB = intcode(dataB, indexB, second_runB, sequence[1], outputA)
            opcodeC, outputC, dataC, indexC, second_runC = intcode(dataC, indexC, second_runC, sequence[2], outputB)
            opcodeD, outputD, dataD, indexD, second_runD = intcode(dataD, indexD, second_runD, sequence[3], outputC)
            opcodeE, outputE, dataE, indexE, second_runE = intcode(dataE, indexE, second_runE, sequence[4], outputD)
            if outputE is not None:
                results.append(int(outputE))
            if opcodeE == 99:
                cont = False

    print("The answer is:", max(results))


main()



