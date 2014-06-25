class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

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

  def __str__(self):
    return self.print_tree(self)