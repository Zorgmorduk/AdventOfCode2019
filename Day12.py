# !/usr/bin/python3
# AdventOfCode2019 - Day12


pos = [[14, 2, 8], [7, 4, 10], [1, 17, 16], [-4, -1, 1]]
vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
pot = [0, 0, 0, 0]
kin = [0, 0, 0, 0]


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


def calculate_energies():
    result = []
    for i in range (4):
        kin_energy = 0
        pot_energy = 0
        for j in range(3):
            pot_energy += abs(pos[i][j])
            kin_energy += abs(vel[i][j])
        tot_energy = pot_energy * kin_energy
        result.append(tot_energy)
    return sum(result)


for i in range(1000):
    apply_gravity_on_velocity()
    apply_velocity_on_position()

print("The answer is:", calculate_energies())
