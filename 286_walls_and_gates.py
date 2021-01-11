class Solution:
    EMPTY_ROOM = 2147483647

    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # find gates
        # For each gate DFS, mark visited room
        m = len(rooms)
        n = len(rooms[0])
        # Find gates and fill answer
        gates = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append([i, j])

        # BFS:
        distance = 1
        while len(gates) != 0:
            gate_num = len(gates)
            for _ in range(gate_num):
                gate = gates.pop()
                next_rooms = self.neighbor_rooms(gate, rooms, m, n)
                new_rooms = []
                for i in next_rooms:
                    if rooms[i[0]][i[1]] == self.EMPTY_ROOM:
                        new_rooms.append(i)
                gates = new_rooms + gates
                for i in new_rooms:
                    rooms[i[0]][i[1]] = distance
            distance += 1
        return rooms

    def neighbor_rooms(self, gate, rooms, m, n):
        i, j = gate
        neighbors = [[i - 1, j], [i + 1, j], [i,  j - 1], [i, j + 1]]
        next_rooms = [k for k in neighbors if 0 <= k[0] <
                      m and 0 <= k[1] < n and rooms[k[0]][k[1]] > 0]
        return next_rooms
# Don't think we need a visited array here. Also we don't need to add gates.... Since they are all already visited in the
# very beginning


# DFS?


test = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
solution = Solution()
ans = solution.wallsAndGates(test)
