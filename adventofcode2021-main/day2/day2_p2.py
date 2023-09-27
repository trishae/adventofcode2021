# read file
commands = open('input.txt', 'r').readlines()

x = 0
y = 0
aim = 0

# loop through file
for i in range(0,len(commands)):
    # check if a "forward" instruction
    if (commands[i].split(" ")[0] == "forward"):
        x += int(commands[i].split(" ")[1])
        y += aim * int(commands[i].split(" ")[1])

    # check if an "down" instruction
    elif (commands[i].split(" ")[0] == "down"):
        aim += int(commands[i].split(" ")[1])

    # check if a "up" instruction
    elif (commands[i].split(" ")[0] == "up"):
        aim -= int(commands[i].split(" ")[1])

print("final horizontal position is "+ str(x) + ", final depth is " + str(y) + ", & their product is " + str(x*y))