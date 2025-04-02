class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Prob 1: Write a function that determines if a tree is symmetric.
# Look at the root. If the root has no children, we are done checking the subtrees. If only one exists, return False. Else, we check the left most node and right most node, and right child with left child.
def is_symmetric(root):
    if not root:
        return True
    return is_mirror(root.left, root.right)
    
def is_mirror(left, right):
    if not left and not right: # Both children are none
         return True
    if not left or not right: # Only one is none
         return False
    return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left) # iterates through left subtree and right subtree

tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(tree))

# Prob 2: Return a list of all root-to-left paths in any order.
# Create a list that goes through every node until it reaches None (DFS).
def binary_tree_paths(root):
    paths = []

    if not root:
        return paths
    current_path = str(root.val)
    if not root.left and not root.right:
        paths.append(current_path)
    if root.left:
       left_path = binary_tree_paths(root.left)
       for node in left_path:
           paths.append(current_path + " -> " + node)
    if root.right:
        right_path = binary_tree_paths(root.right)
        for node in right_path:
           paths.append(current_path + " -> " + node)
    return paths

tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(binary_tree_paths(tree))

# Prob 3: Write a function that returns the minimum difference between the values of any two nodes in a binary search tree.
def min_diff_in_bst(root):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    values = inorder(root)
    min_diff = float('inf')
    for i in range(1, len(values)):
        min_diff = min(min_diff, values[i] - values[i-1])
    return min_diff

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(min_diff_in_bst(root))

# Prob 4: Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node of the tree is now the root of tree and every node has no left child and only one right child.
def increasing_bst(root):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node] + inorder(node.right)

    nodes = inorder(root)  # Get all nodes in sorted order
    new_root = nodes[0]  # The leftmost node becomes the new root
    current = new_root
    
    for node in nodes[1:]:  # Rearrange nodes in a right-only structure
        node.left = None
        current.right = node
        current = node
    
    current.right = None  # Ensure the last node's right child is None
    return new_root
