#!/bin/python

# Write a function that checks to see if a
# binary tree is a binary search tree.

# Phone interview conducted on 2/15/2013

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def InOrderTraversal(node, values):
  if node.left:
    InOrderTraversal(node.left, values)
  values.append(node.value)
  if node.right:
    InOrderTraversal(node.right, values)

def IsBinarySearchTree(node):
  """Return true if the node is the root of a binary search tree."""
  assert node
  values = []
  InOrderTraversal(node, values)

  for i in range(0, len(values) - 1):
    if values[i] > values[i+1]:
      return False

  return True

def main():
  bst = Node(3)
  bst.left = Node(1)
  bst.right = Node(4)

  assert IsBinarySearchTree(bst)

  not_bst = Node(3)
  not_bst.left = Node(5)
  not_bst.right = Node(4)

  assert not IsBinarySearchTree(not_bst)

if __name__ == "__main__":
  main()

