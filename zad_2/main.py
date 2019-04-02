from random import randint


def load_it(file):
    file = open(file)

    file.readline()

    newline = file.readline()
    max_w = int(newline)

    newline = file.readline()
    max_f = int(newline)

    in_data = dict()
    newline = file.readline()
    while newline is not "":
        entry = newline.split(" ")
        # ID = (Price, Weight, Fragile)
        in_data[int(entry[0])] = (int(entry[1]), int(entry[2]), int(entry[3]))

        newline = file.readline()

    return in_data, max_w, max_f


def addition_tuple_to_list(list_of_elements: list, element):
    result = []
    for _, a in enumerate(list_of_elements):
        result.append((a[0] + element[0], a[1] + element[1], a[2] + element[2]))

    return result


def do_the_thing(in_data, max_w, max_f):
    states = dict()
    states[0] = [(0, 0, 0)]

    for index in range(1, len(in_data) + 1):
        item = in_data[index]
        # excluding item with index
        new_state = states[index - 1].copy()

        new_state.extend(addition_tuple_to_list(new_state.copy(), item))

        new_state = list(dict.fromkeys(new_state))
        new_state = sorted(new_state, key=lambda x: (x[0] * 1000000 + x[1] * 1000 + x[2]))

        last_item = (-1, -1, -1)
        clean_state = new_state.copy()
        for _, item in enumerate(new_state):
            if item[1] > max_w or item[2] > max_f:
                clean_state.remove(item)
                continue

            if last_item[0] == item[0]:
                if last_item[1] < item[1] and last_item[2] < item[2]:
                    clean_state.remove(item)
                    continue

                if last_item[1] == item[1]:
                    clean_state.remove((last_item[0], last_item[1], max(last_item[2], item[2])))
                    continue

                if last_item[2] == item[2]:
                    clean_state.remove((last_item[0], max(last_item[1], item[1]), last_item[2]))
                    continue

            last_item = item

        states[index] = clean_state
        print("index: {0}, size: {1}".format(index, len(clean_state)))
    return states


def print_knapsack(states, items):
    with open('out.txt', 'w') as f:
        max_index = max(states.keys())
        row = states[max_index]
        res = []
        best = row[-1]
        print(best[0])
        f.write("%s\n" % best[0])
        checksum_c = 0
        checksum_w = 0
        checksum_f = 0
        for row_index in range(max_index, 0, -1):
            if best not in states[row_index - 1]:
                best = (best[0] - items[row_index][0], best[1] - items[row_index][1], best[2] - items[row_index][2],)
                res.append(row_index + 1)
                checksum_c += items[row_index][0]
                checksum_w += items[row_index][1]
                checksum_f += items[row_index][2]
        print(len(res))
        f.write("%s\n" % len(res))
        for _, s in enumerate(res):
            f.write("%s\n" % s)
        print([checksum_c, checksum_w, checksum_f])
        return res


source_data, bx, cx = load_it("./zadanie2data3.txt")

sx = do_the_thing(source_data, bx, cx)

print_knapsack(sx, source_data)


def generate():
    out = ['100', '100', '10']
    for i in range(1, 101):
        out.append('{0} {1} {2} {3}'.format(i, randint(1, 30), randint(1, 10), randint(0, 1)))

    with open('big_in.txt', 'w') as f:
        for item in out:
            f.write("%s\n" % item)

# generate()
