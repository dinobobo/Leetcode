from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def add_trie(w, node):
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            if 'count' not in node:
                node['count'] = 1
            else:
                node['count'] += 1

        def backtracking(i, node):
            if i == n:
                return ['']
            if i in visited:
                return visited[i]
            word = ""
            ans = []
            while i < n:
                if s[i] not in node:
                    break
                else:
                    word += s[i]
                    node = node[s[i]]
                    if 'count' in node:
                        temp = backtracking(i + 1, trie)
                        if temp != []:
                            visited[i] = temp
                            ans += [word + ' ' + i for i in temp]
                i += 1
            return ans

        visited = {}
        trie = {}
        n = len(s)
        for w in wordDict:
            add_trie(w, trie)
        return [i[:len(i) - 1] for i in backtracking(0, trie)]


ans = Solution()
ans.wordBreak("abcd", ["a", "abc", "b", "cd"])
