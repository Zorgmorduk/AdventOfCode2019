# !/usr/bin/python3
# AdventOfCode2019 - Day1part2

print("Paste the input here and press [Enter] twice: ")
end = ""
data = '\n'.join(iter(input, end)).split("\n")
result = []
result2 = []

for mass in data:
    result.append(int(int(mass) / 3.0) - 2)

for i in result:
    fuel = int(i / 3.0) - 2
    if fuel < 0:
        fuel = 0
    result2.append(fuel)
    while fuel > 0:
        fuel = int(fuel / 3.0) - 2
        if fuel < 0:
            fuel = 0
        result2.append(fuel)

print("The sum of the fuel requirements is: ", sum(result) + sum(result2))

