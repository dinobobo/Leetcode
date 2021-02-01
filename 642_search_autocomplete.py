class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        self.ans = []
        for sent, time in zip(sentences, times):
            for _ in range(time):
                self.add_trie(sent)
        self.node = self.trie
        self.prefix = ''

    def add_trie(self, word):
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        if 'count' not in cur:
            cur['count'] = 1
        else:
            cur['count'] += 1

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.node = self.trie
            self.add_trie(self.prefix)
            self.prefix = ''
            return None
        self.prefix += c
        if c not in self.node:
            self.node = {}
            return None
        self.node = self.node[c]
        ans = []
        self.find_sentences(self.node, '', ans)
        return [i[0] for i in ans]

    def find_sentences(self, node, s, ans):
        for char in node:
            if char == 'count':
                self.insert_string(self.prefix + s, node['count'], ans)
            else:
                self.find_sentences(node[char], s + char, ans)

    def insert_string(self, s, count, ans):
        if len(ans) < 3:
            ans.append([s, count])
        else:
            if count > ans[-1][1] or (count == ans[-1][1] and s < ans[-1][0]):
                ans.pop()
                ans.append([s, count])
        ans.sort(key=lambda x: (-x[1], x[0]))


ans = AutocompleteSystem(
    ["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
ans.input('i')
ans.input(' ')
