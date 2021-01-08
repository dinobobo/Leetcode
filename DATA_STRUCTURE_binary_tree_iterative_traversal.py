# Binary tree traversal inorder, preorder, and postorder with iterative approach.

class tree_node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# In order iterative left -> root -> right
def inorder_it(node):
    if node == None:
        return None

    node_st = []
    while len(node_st) != 0 or node != None:
        while node != None:
            # Visit all the left nodes, obviously you don't want to add the root node
            # None node should be excluded too
            node_st.append(node)
            node = node.left

        node = node_st.pop()  # Pop the most left node
        print(node.val)

        # We want the right node to be visited too
        node = node.right


def inorder_it_2(node):
    node_st = []
    while True:
        if node != None:  # Exhaust all the left nodes DFS
            node_st.append(node)
            node = node.left

        elif len(node_st) != 0:
            # Once the all the left nodes and current nodes are done
            # Go visit the right node, and this basically is a recursive call
            node = node_st.pop()
            print(node.val)
            node = node.right

        else:
            break


def Morris_inorder(node):
    cur = node
    while cur != None:
        if cur.left == None:
            print(cur.val)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            if pre.right == cur:
                pre.right = None
                print(cur.val)
                cur = cur.right
            else:
                pre.right = cur
                cur = cur.left


# Pre order iterative root -> left -> right
def preorder_it(node):
    node_st = []
    node_st.append(node)

    while len(node_st) != 0:
        node = node_st.pop()
        print(node.val)
        if node.right:
            node_st.append(node.right)
        if node.left:
            node_st.append(node.left)


def Morris_preorder(node):
    cur = node
    while cur != None:
        if cur.left == None:
            print(cur.val)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            if pre.right == cur:
                pre.right = None
                cur = cur.right
            else:
                pre.right = cur
                print(cur.val)
                cur = cur.left


# Post order iterative right -> left -> root
def postorder_it_2st(node):
    # The idea is that the order of nodes in the stack is similar to the stack
    # established for a preorder traversal. The INVERSE of the postorder stack
    # is the same as the preorder stack, BUT goes as root -> right -> left.
    # Isn't it obvious if you look at the ordering?
    st_temp = []
    st_post = []
    st_temp.append(node)
    while len(st_temp) != 0:
        node = st_temp.pop()
        st_post.append(node)
        if node.left:  # LEFT first since we are going to pop it and append in the st_post
            st_temp.append(node.left)
        if node.right:
            st_temp.append(node.right)
    for i in st_post[::-1]:
        print(i.val)


def postorder_it_1st(node):
    # The key here is that you push the right child THEN the root into the stack
    # Upon visiting a node with a right child, and this child happens to be on
    # the top of the stack, this node has to be visited.
    node_st = []

    while len(node_st) != 0 or node != None:
        while node != None:
            if node.right != None:
                node_st.append(node.right)
            node_st.append(node)
            node = node.left

        node = node_st.pop()
        if node.right != None and len(node_st) > 0 and node_st[-1] == node.right:
            node_st.pop()
            node_st.append(node)
            node = node.right
        else:
            print(node.val)
            node = None  # Set it to None so that it won't be revisited.


# Without using a stack O(N^2), kinda silly.
def postorder(head):

    temp = head
    visited = set()
    while (temp and temp not in visited):

        # Visited left subtree
        if (temp.left and temp.left not in visited):
            temp = temp.left

        # Visited right subtree
        elif (temp.right and temp.right not in visited):
            temp = temp.right

        # Print node
        else:
            print(temp.val)
            visited.add(temp)
            temp = head


# Test
root = tree_node(3)
first_left = tree_node(5)
first_right = tree_node(1)
root.left = first_left
root.right = first_right
first_left.left = tree_node(10)
first_left.right = tree_node(4)
first_right.left = tree_node(0)
first_right.right = tree_node(14)

inorder_it(root)
inorder_it_2(root)
Morris_inorder(root)

preorder_it(root)
Morris_preorder(root)

postorder_it_2st(root)
postorder_it_1st(root)
