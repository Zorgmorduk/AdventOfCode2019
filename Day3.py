# !/usr/bin/python3
# AdventOfCode2019 - Day3

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
    distances.append(abs(i[0]) + abs(i[1]))

print("The answer is: ", min(distances))
