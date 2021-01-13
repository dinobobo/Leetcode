class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        node_copy = Node(node.val)
        self.visited[node] = node_copy
        for neighbor in node.neighbors:
            if neighbor not in self.visited:
                node_copy.neighbors.append(self.cloneGraph(neighbor))
            else:
                node_copy.neighbors.append(self.visited[neighbor])
        return node_copy

# BFS


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

solution = Solution()
ans = solution.cloneGraph(n1)
