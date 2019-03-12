import collections

from zad_1.tree import KeyNode, DummyNode
from zad_1.utils import add_to_log, tree_print, print_tree, print_matrix


def load_it(file):
    file = open(file)

    newline = file.readline()

    inData = dict()
    while newline is not "":
        entry = newline.split(" ")
        inData[entry[1].split("\n")[0]] = int(entry[0])

        newline = file.readline()

    return sum(inData.values()), collections.OrderedDict(sorted(inData.items()))


def split_it(freq_all, in_data):
    k_v = dict()
    d_v = dict()
    k_n = dict()
    d_n = dict()

    ki = 0
    d_freq = 0
    d_words = []
    for word, freq in in_data.items():
        # print(word, v)
        if freq > 50000:
            k_v[ki + 1] = freq / freq_all
            k_n[ki + 1] = KeyNode(word)

            d_v[ki] = d_freq / freq_all
            d_n[ki] = DummyNode(d_words)
            d_words = []
            d_freq = 0
            ki += 1
        else:
            d_freq = d_freq + freq
            d_words.append(word)

    d_v[ki] = d_freq / freq_all
    d_n[ki] = DummyNode(d_words)

    return d_v, k_v, d_n, k_n


# alg podla knihy
def optimize_it(dummy_probs, key_probs):
    n = len(key_probs) + 1
    e = dict()
    w = dict()
    root_node = dict()

    for i in range(1, n + 1):
        w[(i, i - 1)] = dummy_probs[i - 1]
        e[(i, i - 1)] = dummy_probs[i - 1]

    for l in range(1, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            e[(i, j)] = float("inf")
            w[(i, j)] = w[(i, j - 1)] + key_probs[j] + dummy_probs[j]

            for r in range(i, j + 1):
                t = e[(i, r - 1)] + e[(r + 1, j)] + w[(i, j)]
                if t < e[(i, j)]:
                    e[(i, j)] = t
                    root_node[(i, j)] = r

    return root_node, e[1, n - 1]


def grow_it(start_index, end_index, root_data, dummy_nodes, key_nodes, depth=0):
    root_index = root_data[(start_index, end_index - 1)]
    subtree = key_nodes[root_index]

    add_to_log(depth, subtree.word)
    if start_index < root_index:
        subtree.left = grow_it(start_index, root_index, root_data, dummy_nodes, key_nodes, depth + 1)
    else:
        subtree.left = dummy_nodes[root_index - 1]
        subtree.left.used = True

    if root_index + 1 < end_index:
        subtree.right = grow_it(root_index + 1, end_index, root_data, dummy_nodes, key_nodes, depth + 1)
    else:
        subtree.right = dummy_nodes[root_index]
        subtree.right.used = True

    subtree.used = True
    return subtree


# Where the magic happens

def pocet_porovnani(word):
    return sekvoia.get_word(word)


freqAll, inData = load_it("./dictionary.txt")
dummy, keys, dummyNodes, keyNodes = split_it(freqAll, inData)
root, e_val = optimize_it(dummy, keys)
sekvoia = grow_it(1, len(keyNodes) + 1, root, dummyNodes, keyNodes)

print("Priemerny pocet vyhladanani: " + str(e_val))
print("Hlbka stromu: " + str(len(tree_print)))
print("Struktura stromu: ")
print_tree()

print("Pocet porovnani pre ZOLTAN: " + str(pocet_porovnani("zoltan")))