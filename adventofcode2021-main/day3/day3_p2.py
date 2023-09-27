"""
main
"""
def main():
    # read file
    binaries = open('input.txt', 'r').readlines()

    # convert lists of binaries to integers
    oxygenGeneratorRating = int(''.join(map(str, getOGRating(binaries, getCB(binaries), 0))), 2)
    co2ScrubberRating = int(''.join(map(str, getCO2SRating(binaries, getCB(binaries), 0))), 2)

    print("The life support is " + str(oxygenGeneratorRating * co2ScrubberRating))


"""
recursive function to get oxygen generator rating
"""
def getOGRating(binList, mcb, pos):
    if (len(binList) == 1):
        return binList
    else:
        oGRating = []

        for i in range(0, len(binList)):
            # sanitize string
            binList[i] = binList[i].strip()

            # if binary stream contains most common bit, add to list of candidate ratings
            if (int(binList[i][pos]) == mcb[0][pos]):
                oGRating.append(binList[i])

        return getOGRating(oGRating, getCB(oGRating), pos+1)


"""
recursive function to get CO2 scrubber rating
"""
def getCO2SRating(binList, lcb, pos):
    if (len(binList) == 1):
        return binList
    else:
        cO2SRating = []

        for i in range(0, len(binList)):
            # sanitize string
            binList[i] = binList[i].strip()

            # if binary stream contains least common bit, add to list of candidate ratings
            if (int(binList[i][pos]) == lcb[1][pos]):
                cO2SRating.append(binList[i])

        return getCO2SRating(cO2SRating, getCB(cO2SRating), pos+1)

"""
helper function to get most common bits and least common bits given a list of binaries
"""
def getCB(binList):
    # loop through list
    for i in range(0, len(binList)):
        # initialize empty array to store most common bits
        if (i == 0):
            mcb = [0] * (len(binList[i]))
            lcb = [0] * (len(binList[i]))

        binList[i] = binList[i].strip()

        # loop through each binary stream
        for j in range(0, len(binList[i])):
            # count number of ones per bit column
            mcb[j] += int(binList[i][j])

            # if at the last binary stream, perform calculations
            if (i == len(binList) - 1):
                # if counts of 1s are higher than half the length of the file, then the most common value is 1
                if (mcb[j] >= (len(binList) / 2)):
                    mcb[j] = 1
                    lcb[j] = 0
                else:  # otherwise the most common value is 0
                    mcb[j] = 0
                    lcb[j] = 1

    return [mcb,lcb]

main()