# Simple DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        if len(visited) == len(rooms):
            return True

        def helper(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    helper(i)
        helper(0)
        return len(visited) == len(rooms)
