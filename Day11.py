# !/usr/bin/python3
# AdventOfCode2019 - Day11


def add_leading_zero(x):
    return (5 - len(x)) * "0" + x


def interpret_command(x):
    opcode = x[3:5]
    mode1 = x[2]
    mode2 = x[1]
    mode3 = x[0]
    return [opcode, mode1 + mode2 + mode3]


def turn(robot, output):
    if output == "0":  # left 90 degrees
        if robot[2] == 0 and robot[3] == -1:  # up
            robot = (robot[0], robot[1], -1, 0)  # left
        elif robot[2] == -1 and robot[3] == 0:  # left
            robot = (robot[0], robot[1], 0, 1)  # down
        elif robot[2] == 0 and robot[3] == 1:  # down
            robot = (robot[0], robot[1], 1, 0)  # right
        elif robot[2] == 1 and robot[3] == 0:  # right
            robot = (robot[0], robot[1], 0, -1)  # up
    elif output == "1":  # right 90 degrees
        if robot[2] == 0 and robot[3] == -1:  # up
            robot = (robot[0], robot[1], 1, 0)  # right
        elif robot[2] == 1 and robot[3] == 0:  # right
            robot = (robot[0], robot[1], 0, 1)  # down
        elif robot[2] == 0 and robot[3] == 1:  # down
            robot = (robot[0], robot[1], -1, 0)  # left
        elif robot[2] == -1 and robot[3] == 0:  # left
            robot = (robot[0], robot[1], 0, -1)  # up
    return robot


def replace_ch(data, nr_col, nr_row, ch):
    # replaces the character in the data input (list of strings) located at nr_row, nr_col to ch
    line_to_modify = list(data[nr_row])
    line_to_modify[nr_col] = ch
    data[nr_row] = "".join(line_to_modify)
    return data


def execute(command, index, data, rel_base, panels, robot, first_output):
    index_step = 4  # default
    result = 0
    opcode = int(command[0])
    mode = command[1]

    if opcode == 3:  # input
        index_step = 2
        if mode[0] == "0":  # position mode
            data[int(data[index + 1])] = panels[robot[1]][robot[0]]
        elif mode[0] == "2":  # relative mode
            data[int(data[index + 1]) + rel_base] = panels[robot[1]][robot[0]]

    elif opcode == 4:  # output
        index_step = 2
        if mode[0] == "0":  # position mode
            output = data[int(data[index + 1])]
            if first_output:
                first_output = False
                replace_ch(panels, robot[0], robot[1], output)  # paint
                replace_ch(paint_count, robot[0], robot[1], "x")  # paint count
            else:
                first_output = True
                robot = turn(robot, output)  # turn
                robot = (robot[0] + robot[2], robot[1] + robot[3], robot[2], robot[3])  # move
        elif mode[0] == "2":  # relative mode
            output = data[int(data[index + 1]) + rel_base]
            if first_output:
                first_output = False
                replace_ch(panels, robot[0], robot[1], output)  # paint
                replace_ch(paint_count, robot[0], robot[1], "x")  # paint count
            else:
                first_output = True
                robot = turn(robot, output)  # turn
                robot = (robot[0] + robot[2], robot[1] + robot[3], robot[2], robot[3])  # move
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
            return index, index_step, data, rel_base, panels, robot, first_output
        elif opcode == 6:
            if a == 0:
                index = b
                index_step = 0
            else:
                index_step = 3
            return index, index_step, data, rel_base, panels, robot, first_output
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
            return index, index_step, data, rel_base, panels, robot, first_output

        if mode[2] == "0":
            data[int(data[index + 3])] = str(result)
        elif mode[2] == "2":  # relative mode
            data[int(data[index + 3]) + rel_base] = str(result)
        else:
            data[index + 3] = str(result)

    return index, index_step, data, rel_base, panels, robot, first_output


data = input("Paste the input here and press [Enter]: ")
data = data + ",0" * 65536  # to extend the memory
data = data.split(",")  # all inputs remain str now
index = 0
rel_base = 0
panels = ["0" * 1000] * 1000
replace_ch(panels, 500, 500, "1")
paint_count = panels.copy()
robot = (500, 500, 0, -1)   # x location, y location, direction (0, -1) = facing upwards
first_output = True
command = interpret_command(add_leading_zero(data[index]))
while int(command[0]) != 99:
    index, index_step, data, rel_base, panels, robot, first_output = \
        execute(command, index, data, rel_base, panels, robot, first_output)
    index += index_step
    command = interpret_command(add_leading_zero(data[index]))

nr = 0
for i in paint_count:
    nr += i.count("x")
    print(i)
print("The answer is: ", nr)

