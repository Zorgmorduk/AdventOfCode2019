# !/usr/bin/python3
# AdventOfCode2019 - Day12part2

from math import gcd

pos = [[14, 2, 8], [7, 4, 10], [1, 17, 16], [-4, -1, 1]]
starting_pos = [[14, 2, 8], [7, 4, 10], [1, 17, 16], [-4, -1, 1]]
vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


def lcm(i, j):
    return abs(i * j) // gcd(i, j)


def apply_gravity_on_velocity():
    for k in range(3):
        for i in range(3):
            for j in range(i + 1, 4, 1):
                if pos[i][k] > pos[j][k]:
                    vel[i][k] -= 1
                    vel[j][k] += 1
                elif pos[i][k] < pos[j][k]:
                    vel[i][k] += 1
                    vel[j][k] -= 1


def apply_velocity_on_position():
    for i in range(4):
        for j in range(3):
            pos[i][j] += vel[i][j]


def brute_force():  # don't be surprised if it does not work in this way :)
    apply_gravity_on_velocity()
    apply_velocity_on_position()
    i = 1
    while starting_pos != pos:
        apply_gravity_on_velocity()
        apply_velocity_on_position()
        i += 1
    print("The answer is:", i)


apply_gravity_on_velocity()
apply_velocity_on_position()
i = 1
x_found, y_found, z_found = False, False, False
x, y, z = 0, 0, 0
while not (x_found and y_found and z_found):
    apply_gravity_on_velocity()
    apply_velocity_on_position()
    i += 1
    if (not x_found) and (pos[0][0] == starting_pos[0][0] and pos[1][0] == starting_pos[1][0] and
                          pos[2][0] == starting_pos[2][0] and pos[3][0] == starting_pos[3][0]):
        x_found = True
        x = i
    elif (not y_found) and (pos[0][1] == starting_pos[0][1] and pos[1][1] == starting_pos[1][1] and
                            pos[2][1] == starting_pos[2][1] and pos[3][1] == starting_pos[3][1]):
        y_found = True
        y = i
    elif (not z_found) and (pos[0][2] == starting_pos[0][2] and pos[1][2] == starting_pos[1][2] and
                            pos[2][2] == starting_pos[2][2] and pos[3][2] == starting_pos[3][2]):
        z_found = True
        z = i

print("The answer is:", lcm(x + 1, lcm(y + 1, z + 1)))  # add +1 because the velocities have to be identical too (0).
