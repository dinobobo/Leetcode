from collections import deque


# Work like a graph using BFS
class Solution:
    def openLock(self, deadends, target: str) -> int:
        deadends = set(deadends)
        visited = set(['0000'])
        d = 0
        vertices = deque(['0000'])
        while len(vertices) > 0:
            num = len(vertices)
            for _ in range(num):
                v = vertices.pop()
                if v in deadends:
                    continue
                if v == target:
                    return d
                neighbors = self.get_neighbors(v)
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in deadends:
                        vertices.appendleft(neighbor)
                        visited.add(neighbor)
            d += 1
        return -1

    def get_neighbors(self, v):
        neighbors = []
        for i in range(len(v)):
            for j in [10 + 1, 10-1]:
                neighbors.append(
                    v[: i] + str((int(v[i]) + j) % 10) + v[i + 1:])
        return neighbors


test = ["0201", "0101", "0102", "1212", "2002"]
target = '0202'

solution = Solution()
ans = solution.openLock(test, target)
