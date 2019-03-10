class KeyNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None
        self.used = False

    def get_word(self, word, cost=0):
        cost += 1

        if self.word == word:
            return cost
        elif word > self.word:
            return self.right.get_word(word, cost)
        elif word < self.word:
            return self.left.get_word(word, cost)


class DummyNode:
    def __init__(self, word: []):
        self.word = set(word)
        self.used = False

    def get_word(self, word, cost=0):
        if word in self.word:
            return cost + 1
        return None
