# !/usr/bin/python3
# AdventOfCode2019 - Day6

print("Paste the input here and press [Enter] twice: ")
end = ""
data = '\n'.join(iter(input, end)).split("\n")
orbit_map = []
counter = 0

for i in data:
    orbit_map.append(tuple(i.split(")")))

for i in orbit_map:
    counter += 1  # direct orbits
    pointer = i[0]
    loop = True
    while loop:
        loop = False
        for j in orbit_map:
            if pointer == j[1]:
                counter += 1  # indirect orbits
                pointer = j[0]
                loop = True

print("The answer is:", counter)
