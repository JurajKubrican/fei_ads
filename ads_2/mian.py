import math
import sys

file = open("./cvicenie2data2019.txt")

route = [0]
newline = file.readline()
route.append(int(newline))

while newline is not '':
    newline = file.readline()
    if newline is not '':
        route.append(int(newline))

results = [sys.maxsize for i in range(len(route))]
results[0] = 0
for i, city in enumerate(route):
    for j in range(i + 1, len(route)):
        results[j] = min(results[j], results[i] + math.pow(400 - (route[j] - route[i]), 2))

print(results[len(results)-1])
