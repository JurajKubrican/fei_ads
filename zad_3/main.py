def load_it(file):
    file = open(file)

    first_line = file.readline().split(' ')
    n_v = int(first_line[0])
    n_c = int(first_line[1])

    in_data = []
    newline = file.readline()
    while newline is not "":
        entry = newline.split(" ")
        in_data.append((int(entry[0]), int(entry[1])))
        newline = file.readline()

    return in_data, n_c


def build_graph(clauses, num_clauses):
    graph = dict()
    for i in range(num_clauses):
        graph[str(i)] = set()
        graph['-' + str(i)] = set()

    for key, clause in enumerate(clauses):
        graph[str(-clause[0])].add(str(clause[1]))
        graph[str(-clause[1])].add(str(clause[0]))

    return graph


clauses_, num_clauses_ = load_it('in.txt')
graph_ = build_graph(clauses_, num_clauses_)



print(graph_)
