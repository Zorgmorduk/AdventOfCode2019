# !/usr/bin/python3
# AdventOfCode2019 - Day10

from math import gcd

print("Paste the input here and press [Enter] twice: ")
end = ""
data = '\n'.join(iter(input, end)).split("\n")
options = []  # list of maps with potential monitoring locations indicated by O
solutions = []  # list of solutions corresponding to different monitoring locations
nr_asteroids = []  # list containing the number of visible asteroids per monitoring locations


def replace_ch(data, nr_col, nr_row, ch):
    # replaces the character in the data input (list of strings) located at nr_row, nr_col to ch
    line_to_modify = list(data[nr_row])
    line_to_modify[nr_col] = ch
    data[nr_row] = "".join(line_to_modify)
    return data


def generate_coordinate_pairs(absolute_max):
    # generate coordinate pairs that can be used as coordinate offsets relative to a potential monitoring location
    # to identify visible asteroids
    coordinate_pairs = []
    for i in range(1, absolute_max + 1):
        for j in range(i + 1):
            for k in range(4):
                coordinate_pairs.append((i, j))
            if i != j and j != 0:
                for k in range(4):
                    coordinate_pairs.append((j, i))
    # alternate the coordinates
    for i in range(0, len(coordinate_pairs), 2):
        coordinate_pairs[i + 1] = (coordinate_pairs[i + 1][1], coordinate_pairs[i + 1][0])
    # mask them as positive and negative ((+,+); (-,+); (-,-); (+,-))
    for i in range(0, len(coordinate_pairs), 4):
        coordinate_pairs[i + 1] = (-coordinate_pairs[i + 1][0], coordinate_pairs[i + 1][1])
        coordinate_pairs[i + 2] = (-coordinate_pairs[i + 2][0], -coordinate_pairs[i + 2][1])
        coordinate_pairs[i + 3] = (coordinate_pairs[i + 3][0], -coordinate_pairs[i + 3][1])
    return coordinate_pairs


def count_asteroids(data):
    nr = 0
    for i in data:
        nr += i.count("#")
    return nr


def solve_map(data):

    def identify_non_visible_asteroids(data, x, y):
        dx = x - nr_col_O
        dy = y - nr_row_O
        q = gcd(dx, dy)
        dx = dx // q
        dy = dy // q

        newX = nr_col_O + dx
        newY = nr_row_O + dy
        while (newX <= nr_col_max) and (newX >= 0) and (newY <= nr_row_max) and (newY >= 0):
            if data[newY][newX] == "#":
                if not (newX == x and newY == y):
                    replace_ch(data, newX, newY, "*")
            newX += dx
            newY += dy
        return data

    nr_row_O, nr_col_O = None, None
    for nr_row, row in enumerate(data):
        for nr_col, column in enumerate(row):
            if data[nr_row][nr_col] == "O":  # locate O
                nr_row_O = nr_row
                nr_col_O = nr_col
                break  # from the inner for first
        if nr_col_O is not None:
            break  # from the outer for as well
    right_max_delta = nr_col_max - nr_col_O
    left_max_delta = nr_col_O
    up_max_delta = nr_row_O
    down_max_delta = nr_row_max - nr_row_O
    absolute_max = max(right_max_delta, left_max_delta, up_max_delta, down_max_delta)
    coordinate_pairs = generate_coordinate_pairs(absolute_max)
    solved = False
    for i in coordinate_pairs:
        if ((nr_col_O + i[0]) <= nr_col_max) and ((nr_col_O + i[0]) >= 0) and \
                ((nr_row_O + i[1]) <= nr_row_max) and ((nr_row_O + i[1]) >= 0):
            if data[nr_row_O + i[1]][nr_col_O + i[0]] == "#":
                data = identify_non_visible_asteroids(data, nr_col_O + i[0], nr_row_O + i[1])
    return data


# generate list of maps with potential monitoring locations indicated by "O"
nr_row_max = len(data) - 1
nr_col_max = len(data[-1]) - 1
for nr_row, row in enumerate(data):
    for nr_col, column in enumerate(row):
        if data[nr_row][nr_col] == "#":
            options.append(data.copy())
            options[-1] = replace_ch(options[-1], nr_col, nr_row, "O")

for option in options:
    solutions.append(solve_map(option))

for solution in solutions:
    nr_asteroids.append(count_asteroids(solution))

print("The answer is:", max(nr_asteroids))
