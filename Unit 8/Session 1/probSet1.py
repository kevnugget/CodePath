# Prob 1: Given the TreeNode class, create a binary tree with root value 10, left child 4, and right child 6
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(10, TreeNode(4), TreeNode(6))
print(root.val)
print(root.right.val)
print(root.left.val)

# Prob 2: Given a root of a binary tree with exactly three nodes: return true if the value of the root is equal tro the sum of its two children
def check_tree(root):
    return root.val == root.left.val + root.right.val

print(check_tree(root))

# Prob 3: Given a root of a binary tree with AT MOST 3 nodes: return true if the value of the root is rqual to the sum of its two children
def check_tree2(root):
    if not root: # no root
        return False
    if not root.right and not root.left: # root is a leaf
        return False
    elif root.right and root.left:
        return check_tree(root)
    elif root.left:
        return root.val == root.left.val
    elif root.right:
        return root.val == root.right.val
    return False
    
tree1 = TreeNode(10, TreeNode(10)) 
tree2 = TreeNode(5, TreeNode(3), TreeNode(2)) 
tree3 = TreeNode(5, None, TreeNode(2)) 
tree4 = TreeNode(5) 
tree5 = None
print(check_tree2(tree1)) # True
print(check_tree2(tree2)) # True
print(check_tree2(tree3)) # False
print(check_tree2(tree4)) # False
print(check_tree2(tree5)) # False

# Prob 4: Given a root of a binary tree, find the value of the most left node
def left_most(root):
    if not root:
        return None
    if not root.left:
        return root.val
    else:
        return left_most(root.left)
    
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(5))
print(left_most(tree)) # 4

# Prob 5: Implement left_most iteratively
def left_most2(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.val
print(left_most2(tree)) # 4

# Prob 6: Return a list representing the in-order traversal of the nodes' values
def inorder_traversal(root):
    traversed_tree = []
    if not root:
        return []
    traversed_tree.extend(inorder_traversal(root.left))
    traversed_tree.append(root.val)
    traversed_tree.extend(inorder_traversal(root.right))
    return traversed_tree

tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorder_traversal(tree)) # [1,3,2]

# Prob 7: Write a function that returns the number of nodes in a binary tree
def size(root):
    if not root:
        return 0
    else:
        return 1 + size(root.left) + size(root.right)

tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(size(tree)) # 5 and O(n)

# Prob 8: Write a function that returns true if a node with value is in the tree, false otherwise. Assume tree is balanced.
def find(root, value): # Balanced tree
    if not root:
        return False
    
    if root.val == value:
        return True
    
    return find(root.right, value) or find(root.left, value) # O(n)

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(find(tree, 5)) # True

# Prob 9: Write a function that returns true if a node with value in the BINARY SEARCH tree
def find_bst(root, value): # O(log n)
    if not root:
        return False
    if value > root.val and root.right:
        return find(root.right, value)
    elif value < root.val and root.left:
        return find(root.left, value)
    else:
        return True
    
print(find_bst(tree, 5)) # True
print(find_bst(tree, 10)) # False

# Prob 10: Write a function that traverses all LEAVES of a BST in descending order
def descending_leaves(root):
    if not root:
        return []
    lst = []
    if root and not root.right and not root.left:
        lst.append(root.val)
    lst.extend(descending_leaves(root.right))
    lst.extend(descending_leaves(root.left))
    return lst

tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(descending_leaves(tree)) # 4


