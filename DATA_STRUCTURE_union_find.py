class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n + 1)]
        self._ranks = [1 for i in range(n + 1)]

    def find_halving(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def find_compression(self, u):
        if self._parents[u] != u:
            root = self.find_compression(self._parents[u])
            self._parents[u] = root
        return self._parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False

        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        return True
