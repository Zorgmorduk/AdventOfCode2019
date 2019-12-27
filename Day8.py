# !/usr/bin/python3
# AdventOfCode2019 - Day8


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

    zero_count_layer = []
    zero_count_row = 0
    for layer in layers:
        for row in layer:
            zero_count_row += row.count("0")
        zero_count_layer.append(zero_count_row)
        zero_count_row = 0

    layer_with_fewest_0_digits = layers[zero_count_layer.index(min(zero_count_layer))]

    count1 = 0
    count2 = 0
    for layer in layer_with_fewest_0_digits:
        count1 += layer.count("1")
        count2 += layer.count("2")

    print("The answer is: ", count1 * count2)


main()
