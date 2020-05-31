#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root != None:
            left = root.left
            right = root.right
            if (left == None or right == None):
                return self.minDepth(left)+ self.minDepth(right) + 1

            return min(self.minDepth(left), self.minDepth(right)) + 1
        return 0
# @lc code=end

