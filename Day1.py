# !/usr/bin/python3
# AdventOfCode2019 - Day1

print("Paste the input here and press [Enter] twice: ")
end = ""
data = '\n'.join(iter(input, end)).split("\n")
result = []

for mass in data:
    result.append(int(int(mass) / 3.0) - 2)

print("The sum of the fuel requirements is: ", sum(result))

