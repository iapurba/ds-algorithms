from typing import Counter


class Node:
  def __init__(self, value) -> None:
      self.value = value 
      self.left = None
      self.right = None


class BST:
  def __init__(self, node=None) -> None:
      self.root = node 

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
      return self

    current_node = self.root
    while True:
      if value < current_node.value:
        if current_node.left:
          current_node = current_node.left
        else:
          current_node.left = Node(value)
          return self
      else:
        if current_node.right:
          current_node = current_node.right
        else:
          current_node.right = Node(value)
          return self

  # Search a node
  def search(self, value):
    if self.root:
      current = self.root
      while current:
        if current.value == value:
          return True
        elif value < current.value:
          current = current.left
        else:
          current = current.right
    return False


  def find_min_value(self, node):
    current = node
    while (current.left):
      current = current.left
    return current
    
    
  def node_to_be_deleted(self, value):
    current = self.root
    while current:
      if value == current.value:
        return current
      elif value < current.value:
        current = current.left
      else:
        current = current.right
  

  def delete_node(self, value):
    unwanted_node = self.node_to_be_deleted(value)
    
    if not unwanted_node.left and not unwanted_node.right:
      unwanted_node = None
    elif not unwanted_node.left:
      temp = unwanted_node.right
      unwanted_node.value = temp.value
      unwanted_node.right = None
    elif not unwanted_node.right:
      temp = unwanted_node.left
      unwanted_node.value = temp.value
      unwanted_node.left = None
    else:
      inorder_successor = self.find_min_value(unwanted_node.right)
      unwanted_node.value = inorder_successor.value
      inorder_successor = None
    return self



  def inorder(self):
    def traverse_inorder(node):
      if node:
        traverse_inorder(node.left)
        print(str(node.value), '->', end=' ')
        traverse_inorder(node.right)
    
    return traverse_inorder(self.root)

  
root = BST()
root.insert(8)
root.insert(7)
root.insert(12)
root.insert(2)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(4)
root.insert(6)
root.insert(10)
root.insert(9)
root.insert(11)
root.insert(14)
root.insert(13)
root.insert(15)


print(root.delete_node(13))
root.inorder()

