# Brute force, Time Limited Error
from collections import Counter
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # convert to sets
        word_set = [set(list(word)) for word in words]
        puzzle_set = [set(list(puzzle)) for puzzle in puzzles]
        heads = [puzzle[0] for puzzle in puzzles]
        ans = []
        for i in range(len(puzzle_set)):
            head = heads[i]
            count = 0
            for word in word_set:
                # check validity of the word
                if head in word:
                    is_valid = True
                    for char in word:
                        if char not in puzzle_set[i]:
                            is_valid = False
                            break
                    if is_valid == True:
                        count += 1
            ans.append(count)
        return ans


# Seach if words match sub-string


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        # words to sets
        word_set = [frozenset(word) for word in words]
        count = Counter(word_set)
        ans = []

        for p in puzzles:
            # find sub-strings with dp
            subs = [p[0]]
            for char in p[1:]:
                subs += [char + i for i in subs]
            # count occurance of these sub strings
            valids = 0
            for sub in subs:
                if frozenset(sub) in count:
                    valids += count[frozenset(sub)]
            ans.append(valids)
        return ans

# Use bit mask to create the set and the substrings.


# Implement with a Trie!


ans = Solution()
words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
ans.findNumOfValidWords(words, puzzles)
