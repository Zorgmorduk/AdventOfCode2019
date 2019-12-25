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


command = interpret_command(add_leading_zero(data[index]))
while int(command[0]) != 99:
    index_step = 4
    if int(command[0]) == 1:  # addition with three parameters
        if command[1] == "000":  # all are in position mode
            data[int(data[index + 3])] = str(int(data[int(data[index + 1])]) + int(data[int(data[index + 2])]))
        elif command[1] == "001":
            data[int(data[index + 3])] = str(int(data[int(data[index + 1])]) + int(data[index + 2]))
        elif command[1] == "010":
            data[int(data[index + 3])] = str(int(data[index + 1]) + int(data[int(data[index + 2])]))
        elif command[1] == "100":
            data[index + 3] = str(int(data[int(data[index + 1])]) + int(data[int(data[index + 2])]))
        elif command[1] == "011":
            data[int(data[index + 3])] = str(int(data[index + 1]) + int(data[index + 2]))
        elif command[1] == "110":
            data[index + 3] = str(int(data[index + 1]) + int(data[int(data[index + 2])]))
        elif command[1] == "101":
            data[index + 3] = str(int(data[int(data[index + 1])]) + int(data[index + 2]))
        elif command[1] == "111":  # all are in immediate mode
            data[index + 3] = str(int(data[index + 1]) + int(data[index + 2]))
    elif int(command[0]) == 2:  # multiplication
        if command[1] == "000":  # all are in position mode
            data[int(data[index + 3])] = str(int(data[int(data[index + 1])]) * int(data[int(data[index + 2])]))
        elif command[1] == "001":
            data[int(data[index + 3])] = str(int(data[int(data[index + 1])]) * int(data[index + 2]))
        elif command[1] == "010":
            data[int(data[index + 3])] = str(int(data[index + 1]) * int(data[int(data[index + 2])]))
        elif command[1] == "100":
            data[index + 3] = str(int(data[int(data[index + 1])]) * int(data[int(data[index + 2])]))
        elif command[1] == "011":
            data[int(data[index + 3])] = str(int(data[index + 1]) * int(data[index + 2]))
        elif command[1] == "110":
            data[index + 3] = str(int(data[index + 1]) * int(data[int(data[index + 2])]))
        elif command[1] == "101":
            data[index + 3] = str(int(data[int(data[index + 1])]) * int(data[index + 2]))
        elif command[1] == "111":  # all are in immediate mode
            data[index + 3] = str(int(data[index + 1]) * int(data[index + 2]))
    elif int(command[0]) == 3:  # input
        index_step = 2
        data[int(data[index + 1])] = input("Please provide your input:")
    elif int(command[0]) == 4:  # output
        index_step = 2
        print(data[int(data[index + 1])])
    index += index_step
    if index <= len(data):  # just safety check to avoid running out of index bounds, but input data should prevent this
        command = interpret_command(add_leading_zero(data[index]))
    else:
        command = ["99", "0", "0", "0"]
