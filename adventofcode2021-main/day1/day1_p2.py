# read file
depthMeasurements = open('input.txt', 'r')
measurements = depthMeasurements.readlines()

increases = 0
curWindowSum = 0
nextWindowSum = 0

# loop through file
for i in range(0,len(measurements)-3):
    # get sum of current sliding window
    curWindowSum = int(measurements[i]) + int(measurements[i+1]) + int(measurements[i+2])

    # get sum of next sliding window
    nextWindowSum = int(measurements[i+1]) + int(measurements[i+2]) + int(measurements[i+3])

    # increment increases if next sum is larger than current sum
    if (nextWindowSum > curWindowSum):
        increases+=1

print("number of window measurement increases is " + str(increases))