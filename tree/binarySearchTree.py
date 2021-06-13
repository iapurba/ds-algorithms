#!/usr/bin/env python3

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


# Depth first traversal preorder, inroder & postorder.
# Here we have taken an extra array as parameter to store the node value,
# so the it will help to visualize the order

# Preorder traversal
def dfs_preorder(root, result):
    if root:
        # Visit node
        # And push the node value into the result list
        result.append(root.key)

        # Visit left
        dfs_preorder(root.left, result)

        # Visit right
        dfs_preorder(root.right, result)

    return result


# Inorder traversal
def dfs_inorder(root, result):
    if root:
        # Visit left
        dfs_inorder(root.left, result)

        # Visit node
        # And push the node value into the result list
        result.append(root.key)

        # Visit right
        dfs_inorder(root.right, result)
    
    return result


# Postorder traversal
def dfs_postorder(root, result):
    if root:
        # Visit left
        dfs_postorder(root.left, result)

        # Visit right
        dfs_postorder(root.right, result)

        # Visit node
        # And push the node value in the result list
        result.append(root.key)
    
    return result


# Breadth first traversal
def bfs(root):
    if not root:
        return
    
    queue = []
    queue.append(root)
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.key)
        
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    
    return result

    
    
if __name__ == "__main__":
    root = None

    root = insert(root, 10)
    root = insert(root, 7)
    root = insert(root, 11)
    root = insert(root, 6)
    root = insert(root, 1)
    root = insert(root, 8)
    root = insert(root, 9)
    root = insert(root, 20)
    root = insert(root, 22)
    root = insert(root, 14)

    # delete_node(root, 9)

    # Remeber as above the functions defination,
    # we must send and empty array to store the visited node values
    print("DFS Preorder:", dfs_preorder(root, []))

    print("DFS Inorder:", dfs_inorder(root, []))

    print("DFS Postorder:", dfs_inorder(root, []))

    print("Breadth first traversal:", bfs(root))
