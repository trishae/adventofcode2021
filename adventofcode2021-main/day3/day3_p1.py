# read file
binaries = open('input.txt', 'r').readlines()

# loop through file
for i in range(0, len(binaries)):
    # initialize empty array to store most common bits (gamma) and least common bits (epsilon)
    if (i == 0):
        mcb = [0] * (len(binaries[i])-1)
        lcb = [0] * (len(binaries[i])-1)

    # sanitize string
    binaries[i] = binaries[i].strip()

    # loop through each binary stream
    for j in range(0, len(binaries[i])):
        # count number of ones per bit column
        mcb[j] += int(binaries[i][j])

        # if at the last binary stream, perform calculations
        if (i == len(binaries)-1):
            # if counts of 1s are higher than half the length of the file, then the most common value is 1
            if (mcb[j] >= (len(binaries)/2)):
                mcb[j] = 1
                lcb[j] = 0
            else: # otherwise the most common value is 0
                mcb[j] = 0
                lcb[j] = 1

# convert lists of binaries to integers
gamma = int(''.join(map(str, mcb)), 2)
epsilon = int(''.join(map(str, lcb)), 2)

print("The power consumption is " + str(gamma * epsilon))
