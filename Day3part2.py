# !/usr/bin/python3
# AdventOfCode2019 - Day3part2

print("Paste the input here and press [Enter] twice: ")
end = ""
data = "\n".join(iter(input, end)).split("\n")
wire1 = data[0]
wire2 = data[1]


def process_wire(wire_data):
    wire_map = []
    x = 0
    y = 0
    for i in wire_data:
        if i[0] == "U":
            for j in range(int(i[1:])):
                y += 1
                wire_map.append((x, y))
        elif i[0] == "D":
            for j in range(int(i[1:])):
                y -= 1
                wire_map.append((x, y))
        elif i[0] == "R":
            for j in range(int(i[1:])):
                x += 1
                wire_map.append((x, y))
        elif i[0] == "L":
            for j in range(int(i[1:])):
                x -= 1
                wire_map.append((x, y))
    return wire_map


wire1 = process_wire(wire1.split(","))
wire2 = process_wire(wire2.split(","))

intersections = list(set(wire1).intersection(set(wire2)))

distances = []
for i in intersections:
    distance = 0
    for w1 in wire1:
        if w1 != i:
            distance += 1
        else:
            distance += 1
            break
    for w2 in wire2:
        if w2 != i:
            distance += 1
        else:
            distance += 1
            break
    distances.append(distance)

print("The answer is: ", min(distances))
