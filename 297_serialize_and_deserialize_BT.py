class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.ans = ''
        self.i = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            self.ans += 'None,'
        else:
            self.ans += (str(root.val) + ',')
            self.serialize(root.left)
            self.serialize(root.right)
        return self.ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper():
            if data[self.i] == 'None':
                self.i += 1
                return None
            else:
                root = TreeNode(int(data[self.i]))
                self.i += 1
                root.left = helper()
                root.right = helper()

            return root

        data = data.split(',')
        print(data)
        return helper()


test = TreeNode(1)
test.left = TreeNode(2)
test.right = TreeNode(3)
test.right.left = TreeNode(4)
test.right.right = TreeNode(5)

ans = Codec()
print(ans.serialize(test).split(','))
