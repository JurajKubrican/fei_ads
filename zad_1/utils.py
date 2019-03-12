import json

tree_print = dict()


def add_to_log(depth, word):
    if depth in tree_print:
        tree_print[depth].append(word)
    else:
        tree_print[depth] = [word]


def print_tree():
    for v in tree_print.values():
        print(v)


def save_to_file(data, filename):
    data2 = dict()
    for k, v in data.items():
        key = repr(k)
        data2[key] = v
    f = open(filename, 'w')
    f.write(json.dumps(data2, indent=2))
    f.close()


def print_matrix(in_data, size=152):
    matrix = [[0 for _ in range(size)]
              for _ in range(size)]
    for k, v in in_data.items():
        print(v)
        # matrix[k[0]][k[1]] = v

    for i in range(size):
        for j in range(size):
            print(" {0:0=2d}".format(matrix[i][j]), end='')
        print()
