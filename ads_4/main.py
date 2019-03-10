file = open("./cvicenie4data2019.txt")

inData = []

newline = file.readline()

while newline is not "":
    numbers = []
    for i in newline.split(","):
        numbers.append(int(i))
    inData.append(numbers)
    newline = file.readline()

file.close()

results = [[0 for i in range(2001)]
           for j in range(len(inData)-1)]
for i in range(1, len(results)):
    for j in range(1, len(results[0])):
        results[i][j] = results[i - 1][j]
        if inData[i - 1][1] > j:
            candidate = results[i - 1][j - inData[i - 1][1]] + inData[i - 1][0]
            if candidate > results[i][j]:
                results[i][j] = candidate

        if inData[i - 1][3] > j:
            candidate = results[i - 1][j - inData[i - 1][3]] + inData[i - 1][2]
            if candidate > results[i][j]:
                results[i][j] = candidate

print(results[-1][-1])
