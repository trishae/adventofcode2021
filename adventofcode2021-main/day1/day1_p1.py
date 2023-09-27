# read file
depthMeasurements = open('input.txt', 'r')
measurements = depthMeasurements.readlines()

increases = 0

# loop through file
for i in range(1,len(measurements)):
    # increment increases if current value is larger than previous
    if (int(measurements[i]) > int(measurements[i-1])):
        increases+=1

print("number of depth measurement increases is " + str(increases))