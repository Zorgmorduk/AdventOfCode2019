# !/usr/bin/python3
# AdventOfCode2019 - Day2

data = input("Paste the input here and press [Enter]: ")
data = data.split(",")
data = list(map(int, data))
data[1] = 12
data[2] = 2
index = 0

command = data[index]
while command != 99:
    if command == 1:  # addition
        data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
    elif command == 2:  # multiplication
        data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
    index += 4
    if index <= len(data):  # just safety check to avoid running out of index bounds, but input data should prevent this
        command = data[index]
    else:
        command = 99

print("The answer is: ", data[0])
