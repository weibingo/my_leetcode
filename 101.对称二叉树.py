#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            left = root.left
            right = root.right
            return self.isSymmetric0(left, right)
        return True
    

    def isSymmetric0(self, p: TreeNode, q: TreeNode) -> bool:   
        if p and q:
            return (p.val == q.val) and self.isSymmetric0(p.left, q.right) and self.isSymmetric0(q.left, p.right) 
        return p is q
# @lc code=end

