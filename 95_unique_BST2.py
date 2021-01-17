class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(l, r):
            if l >= r:
                return [None]
            ans = []
            for mid in range(l, r):
                left_nodes = helper(l, mid)
                right_nodes = helper(mid + 1, r)
                for i in left_nodes:
                    for j in right_nodes:
                        node = TreeNode(mid)
                        node.left = i
                        node.right = j
                        ans.append(node)
            return ans
        if n == 0:
            return []
        return helper(1, n + 1)

# Using Dynamic programming?
# Use Hashmap to save the left tree and right tree result?


solution = Solution()
ans = solution.generateTrees(3)
