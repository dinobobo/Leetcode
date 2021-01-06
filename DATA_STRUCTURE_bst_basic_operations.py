class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# Insert Key
def insert(root, key):
    if not root:
        return Node(key)
    elif root.val > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def insert_it(root, key):
    #Need to keep track of the parent node that will have the child as the inserted node
    if not root:
        return Node(key)
    
    p = root
    c = root
    #Use one pointer to traverse the tree and the other to keep track of the parent of this node
    #so that we can insert the key
    while c != None:
        p = c
        if c.val < key:
            c = c.right
        else:
            c = c.left

    #Insert the key as c == None now
    if p.val < key:
        p.right = Node(key)
    else:
        p.left = Node(key)
    return root


# Travesal in order

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def inorder_it(root):
    st = []
    node = root
    st.append(node)
    while len(st) != 0: 
        while node != None: # Go on left node to the end and then back track to the right
            st.append(node)
            node = node.left
        node = st.pop(-1)
        print(node.val)
        node = node.right
    

def postorder(root):
    if root:
        postorder(root.right)
        print(root.val)
        postorder(root.left)

def BST_min(node):
    if not node:
        return None

    while node.left:
        node = node.left
    return node


def BST_max(node):
    if not node:
        return None
    
    while node.right:
        node = node.right
    return node
    
def successor(node):
    # If there node.right != None then min(node.right) is the return
    if node.right != None:
        return BST_min(node.right)
    # If there node.right == None, then it has to be the closest ancester that has a left child 
    # that is also the ancestor of the node
    # obviousely it requires a parent pointer
    p = node.parent
    while p != None and node == p.right:
        node = p
        p = p.parent
    return p

        
def predecessor(node):
    if node.left != None:
        return BST_max(node.left)
    
    p = node.parent
    while p != None and node == p.left:
        node = p
        p = p.parent
    return p


def delete(root, node):
    # Four cases to handle, see CLRS 298
    if root == None:
        return root
    
    # Find the node first
    if root.val > node.val:
        root.left = delete(root.left, node) # delete has to return the spliced node
    elif root.val < node.val:
        root.right = delete(root.right, node)
    else: # node = root
        if node.left == None:
            temp = node.right
            node = None # end this node, since it's not in use anymore
            return temp
        elif node.right == None:
            temp = node.left
            node = None
            return temp
        else:
            # Trick case, when node has both children. The node has to be replaced by its successor
            suc = BST_min(node.right)
            if suc == node.right:
                # easy case, we replace node with suc and it's obvious that suc has no left child
                temp = node.right
                node == None
                return temp
            else:
                # In this case, suc has to be replaced by its right child
                # node also has to be replaced by suc, and suc.right = node.right
                root.val = suc.val
                root.right = delete(root.right, suc)
    return root




    pass








#Test

root = Node(8)
node_l = Node(3)
node_r = Node(10)
node_l.left = Node(1)
node_l.right = Node(6)
node_r.left = Node(9)
node_r.right = Node(15)
root.left = node_l
root.right = node_r

# Print inorder
inorder(root)
postorder(root)



# Test insertion
insert_it(root, 3.3)
inorder(root)
inorder_it(root)

# Test deletion


