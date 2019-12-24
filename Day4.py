# !/usr/bin/python3
# AdventOfCode2019 - Day4

low = "146810"
high = "612564"
current = low
solutions = []


def two_digits_same(s):
    for x in range(len(s) - 1):
        if s[x] == s[x + 1]:
            return True
    return False


def digits_never_decrease(s):
    for y in range(len(s) - 1):
        if s[y] > s[y + 1]:
            return False
    return True


for i in range(int(low), int(high) + 1):
    if two_digits_same(str(i)) and digits_never_decrease(str(i)):
        solutions.append(i)

print("The answer is:", len(solutions))
