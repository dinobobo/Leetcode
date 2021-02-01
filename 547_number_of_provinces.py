# Simple DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def DFS(city):
            if city not in visited:
                visited.add(city)
                for col in range(n):
                    if isConnected[city - 1][col] == 1:
                        DFS(col + 1)

        n = len(isConnected)
        ans = 0
        visited = set()
        for city in range(1, n + 1):
            if city not in visited:
                DFS(city)
                ans += 1
        return ans
