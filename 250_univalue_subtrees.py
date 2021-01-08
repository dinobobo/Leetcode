class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node):
            if node.left:
                is_left = helper(node.left)
                if not node.right:
                    if is_left and node.left.val == node.val:
                        self.ans += 1
                        return True
                    else:
                        return False
                else:
                    is_right = helper(node.right)
                    if is_left and is_right and node.left.val == node.right.val == node.val:
                        self.ans += 1
                        return True
                    else:
                        return False
            else:
                if node.right:
                    is_right = helper(node.right)
                    if is_right and node.right.val == node.val:
                        self.ans += 1
                        return True
                    else:
                        return False
                else:
                    self.ans += 1
                    return True
        helper(root)
        return self.ans

# It can be vastly simplified code wise. Consider check node.val with node.left.val and
# node.right.val with in the recursive calls. Also, return True for None but not increment
# the count, so that we don't have to deal with all the cases.


ans = Solution()
test = TreeNode(2, TreeNode(2), TreeNode(2))
ans.countUnivalSubtrees(test)
