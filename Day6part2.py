# !/usr/bin/python3
# AdventOfCode2019 - Day6part2

print("Paste the input here and press [Enter] twice: ")
end = ""
data = '\n'.join(iter(input, end)).split("\n")
orbit_map = []

for i in data:
    orbit_map.append(tuple(i.split(")")))


def route2com(start):
    route = []
    loop = True
    pointer = start
    while loop:
        loop = False
        for j in orbit_map:
            if pointer == j[1]:
                pointer = j[0]
                loop = True
                route.append(j)
    return route


intersections = []
san2com = route2com("SAN")
me2com = route2com("YOU")
for i1, val1 in enumerate(san2com):
    for i2, val2 in enumerate(me2com):
        if val1[0] == val2[0]:
            intersections.append((i1 + i2, val1[0]))

intersections.sort(key=lambda tup: tup[0])
print("The answer is:", intersections[0][0])
