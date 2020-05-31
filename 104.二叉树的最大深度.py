#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root != None:
            left = root.left
            right = root.right
            if (left == None or right == None):
                return self.maxDepth(left)+ self.maxDepth(right) + 1

            return max(self.maxDepth(left), self.maxDepth(right)) + 1
        return 0
# @lc code=end

