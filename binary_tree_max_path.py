# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from treenode import TreeNode

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if (root == None):
            return 0
        left  = self.bfsSum(root.left)
        right = self.bfsSum(root.right)

        return left + right + root.val

    def bfsSum(self, root):
        if root == None:
            return 0
        queue  = deque([])
        sums   = {root: root.val}
        maxSum = root.val
        queue.append(root)
        while queue:
            curr = queue.popleft()
            curr_sum = sums[curr]
            if curr.left:
                sums[curr.left] = curr_sum + curr.left.val
                queue.append(curr.left)
                maxSum = max(maxSum, sums[curr.left])
            if curr.right:
                sums[curr.right] = curr_sum + curr.right.val
                queue.append(curr.right)
                maxSum = max(maxSum, sums[curr.right])
            del(sums[curr])

        return maxSum


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(7)
root.left.left.left = TreeNode(9)
root.left.left.right = TreeNode(8)


root.right = TreeNode(5)
root.right.right = TreeNode(6)

print root.print_tree(root)
print '----------------'

s = Solution()
print s.maxPathSum(root)