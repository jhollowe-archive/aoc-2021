def threeWindowSum(list, base_index):
    return int(list[base_index]) + int(list[base_index+1]) + int(list[base_index+2])


with open("input/1.txt", "r") as inFile:
    lines = inFile.readlines()

    # part 1
    larger = [x for x in range(1, len(lines)) if int(
        lines[x]) > int(lines[x-1])]

    # part 2
    largerWindow = [x for x in range(
        1, len(lines)-2) if threeWindowSum(lines, x) > threeWindowSum(lines, x-1)]


print("part 1:", len(larger))
print("part 2:", len(largerWindow))
