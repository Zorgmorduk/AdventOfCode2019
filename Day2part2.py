# !/usr/bin/python3
# AdventOfCode2019 - Day2part2

data = input("Paste the input here and press [Enter]: ")
data = data.split(",")
data = list(map(int, data))
memory = data.copy()

for i in range(100):
    for j in range(100):
        memory = data.copy()
        memory[1] = i
        memory[2] = j
        index = 0

        command = memory[index]
        while command != 99:
            if command == 1:  # addition
                memory[memory[index + 3]] = memory[memory[index + 1]] + memory[memory[index + 2]]
            elif command == 2:  # multiplication
                memory[memory[index + 3]] = memory[memory[index + 1]] * memory[memory[index + 2]]
            index += 4
            if index <= len(memory) + 3:  # just safety check to avoid running out of index bounds
                command = memory[index]
            else:
                command = 99
            if memory[0] == 19690720:
                print("The noun is: ", memory[1])
                print("The verb is: ", memory[2])
                print("The answer is:", memory[1] * 100 + memory[2])
                exit(0)
