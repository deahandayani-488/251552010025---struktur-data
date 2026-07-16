class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Membangun Binary Tree
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traversal Functions (return list)
def preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)
    return result

def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)
    return result

def postorder(node, result=None):
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)
    return result

# Get results
pre = preorder(root)
ino = inorder(root)
post = postorder(root)


print("Preorder:", pre)
print("Inorder:", ino)
print("Postorder:", post)

print()
