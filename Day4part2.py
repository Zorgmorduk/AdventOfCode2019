# !/usr/bin/python3
# AdventOfCode2019 - Day4part2

low = "146810"
high = "612564"
current = low
solutions = []


def at_least_two_digits_same(s):
    digits = [("0", 0)]  # (digit, count)
    for x in s:
        if x not in digits:
            digits.append((x, s.count(x)))
    if 2 in [k[1] for k in digits]:
        return True
    else:
        return False


def digits_never_decrease(s):
    for y in range(len(s) - 1):
        if s[y] > s[y + 1]:
            return False
    return True


for i in range(int(low), int(high) + 1):
    if at_least_two_digits_same(str(i)) and digits_never_decrease(str(i)):
        solutions.append(i)

print("The answer is:", len(solutions))
