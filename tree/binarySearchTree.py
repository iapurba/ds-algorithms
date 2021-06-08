# Binary Search Tree (BST) operations in python

# Create a node
class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)

        # Traverse node
        print(str(root.key), '->', end=' ')

        # Traverse right
        inorder(root.right)


def find_min_value(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete_node(root, key):
    # Return if the tree is empty
    if not root:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children, find the inorder successor
        # and place it in position of node to be deleted
        temp = find_min_value(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.key)

    return root




root = None
root = insert(root, 15)
root = insert(root, 10)
root = insert(root, 11)
root = insert(root, 13)
root = insert(root, 26)
root = insert(root, 17)
root = insert(root, 31)
root = insert(root, 2)
root = insert(root, 6)
root = insert(root, 4)
print(inorder(root))
delete_node(root, 17)
print(inorder(root))
