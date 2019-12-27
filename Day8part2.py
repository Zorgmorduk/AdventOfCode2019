# !/usr/bin/python3
# AdventOfCode2019 - Day8part2


def main():
    data = input("Paste the input here and press [Enter]: ")
    width = 25
    height = 6
    layers = []
    layer = []
    counter = 0

    for i in range(0, len(data), width):
        layer.append(data[i: i + width])
        counter += 1
        if counter == height:
            counter = 0
            layers.append(layer)
            layer = []

    class BG:
        black = '\033[40m'
        red = '\033[41m'
        reset = '\033[0m'

    for y in range(height):
        print(BG.reset)
        for x in range(width):
            for layer in layers:
                if layer[y][x] == "2":
                    continue
                else:
                    if layer[y][x] == "1":
                        print(BG.red, layer[y][x], end=" ")
                    else:
                        print(BG.black, layer[y][x], end=" ")
                    break


main()
