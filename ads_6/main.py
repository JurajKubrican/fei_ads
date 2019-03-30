import copy

file = open("./cvicenie6data2019.txt")

newline = file.readline()
n = int(newline)

distances = [[0 for i in range(n)] for j in range(n)]

newline = file.readline()
row = 0
while newline is not "":
    for k, v in enumerate(newline.split(" ")):
        distances[row][k] = int(v)
    row += 1
    newline = file.readline()

file.close()

memo = {}
result = []
for i in range(1, n):
    memo[i, ()] = distances[i][0]


def get_min(from_city, mask):
    if (from_city, mask) in memo:
        return memo[(from_city, mask)]

    values = []

    for city in mask:
        tmp_mask = copy.deepcopy(list(mask))
        tmp_mask.remove(city)

        tmp_min = get_min(city, tuple(tmp_mask))
        values.append(distances[from_city - 1][city - 1] + tmp_min)

    min_result = min(values)
    memo[(from_city, mask)] = min_result

    return min_result


shortest = get_min(0, tuple(range(1, n)))
print(shortest)
