#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        all = []
        while (root is not None):
            node = [root.val]
            all.append(node)
            lr = self.levelAdd(root)
            all.append(lr)
            left = root.left
            right = root.right
            
        

    def levelAdd(self, root: TreeNode) -> List[int]:
        node = []
        if (root is not None):
            left = root.left
            right = root.right
            if (left is not None):
                node.append(left.val)
            right (right is not None):
                node.append(right.val)
        return node
# @lc code=end

