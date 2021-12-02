# part 1
with open("input/2.txt", "r") as inFile:
    lines = inFile.readlines()
    depth = 0
    horiz = 0
    for line in lines:
        command, scale = line.split(" ")

        if (command == "up"):
            depth -= int(scale)
        elif (command == "down"):
            depth += int(scale)
        elif (command == "forward"):
            horiz += int(scale)

print(f"part1: {depth}*{horiz}={depth*horiz}")

# part 2
with open("input/2.txt", "r") as inFile:
    lines = inFile.readlines()
    depth = 0
    horiz = 0
    aim = 0
    for line in lines:
        command, scale = line.split(" ")

        if (command == "up"):
            aim -= int(scale)
        elif (command == "down"):
            aim += int(scale)
        elif (command == "forward"):
            horiz += int(scale)
            depth += aim * int(scale)

print(f"part2: {depth}*{horiz}={depth*horiz}")
