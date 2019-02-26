file = open("./cvicenie3data2019.txt")

matrix = []

newline = file.readline()

while newline is not "":
    numbers = []
    for i in newline.split(" "):
        numbers.append(int(i))
    matrix.append(numbers)
    newline = file.readline()

file.close()

results = [[0 for i in range(len(matrix[0]))]
           for j in range(len(matrix))]

results[0] = matrix[0]
for row in range(1, len(matrix)):
    for col in range(len(matrix[0])):
        results[row][col] = min(
            results[row - 1][max(col - 1, 0)],
            results[row - 1][col],
            results[row - 1][min(col + 1, len(matrix[0]) - 1)]
        ) + matrix[row][col]
print(min(results[-1]))
