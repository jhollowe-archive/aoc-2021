
with open("input/3.txt", "r") as inFile:
    lines = inFile.readlines()

    bit_counts = [0] * len(lines[0].strip())
    gamma = ""
    epsilon = ""
    for line in lines:
        line = line.strip()
        for i in range(len(line)):
            bit_counts[i] += int(line[i])

    for bit in bit_counts:
        if bit > len(lines)/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    val = int(gamma, 2) * int(epsilon, 2)


print(f"part1: {val}")
