def load_it(file):
    file = open(file)

    newline = file.readline()
    int_data = [0]

    for c in newline:
        int_data.append(int(c))

    return int_data


in_data = load_it('cvicenie5data2019.txt')

n = len(in_data)

results = [[9999999 for i in range(n + 1)]
           for j in range(n + 1)]

history = [[0 for i in range(n + 1)]
           for j in range(n + 1)]

for l in range(1, n):
    for r in range(n, n - l):
        results[l][r] = \
            min(results[l][r - 1], results[l - 1][r]) + \
            min(in_data[l], in_data[r - 1])

best1 = min(results[n])
best2 = min(results[:][n])

print(results[n - 1])
print(results[:][n - 1])
