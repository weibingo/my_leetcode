#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if (root is None):
            return True
        return self.rec(root) != -1
        # left = root.left
        # right = root.right
        # return self.isBalanced(left) and self.isBalanced(right) and (abs(self.depth(left) - self.depth(right)) <= 1)

    def depth(self, root: TreeNode) -> int:
        if (root is None):
            return 0
        return max(self.depth(root.left), self.depth(root.right)) +1

    def rec(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.rec(root.left)
        if (left == -1):
            return -1
        right = self.rec(root.right)
        if (right == -1):
            return -1
        if (abs(left - right) > 1):
            return -1
        else:
            return max(left, right) + 1
# @lc code=end

