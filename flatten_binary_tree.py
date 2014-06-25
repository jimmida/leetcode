# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return nothing, do it in place
  def __init__(self):
    self.root0 = None
    self.stack = []

  def flatten(self, root):
    self.flatten2(root)
    curr = root
    while curr != None:
        curr.right = curr.left
        curr.left  = None
        curr       = curr.right

  def flatten2(self, root):
    if root == None:
      if self.stack == []:
       return
      last = self.stack.pop()
      parent = last
      while last.right == None:
        if self.stack == []:
          return
        last = self.stack.pop()
      root = last.right
      parent.left = root
      last.right = None

    self.stack.append(root)

    self.flatten2(root.left)

  def print_tree(self, root, depth=0):
    ret = ""

    # Print right branch
    if root.right != None:
      ret += self.print_tree(root.right, depth + 1)

    # Print own value
    ret += "\n" + ("    "*depth) + str(root.val)

    # Print left branch
    if root.left != None:
      ret += self.print_tree(root.left, depth + 1)

    return ret


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)

s = Solution()
print s.print_tree(root)
print '----------'
s.flatten(root)
print s.print_tree(root)