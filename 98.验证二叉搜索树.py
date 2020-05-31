#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res=[]
        self.inorder(root, res)
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False
        return True
        # if (root is None):
        #     return True
        # return self.is_val(root,-(2**32),2**32)

    def is_val(self,node, min_v, max_v):
        if node == None:
            return True
        if node.left!= None:
            if node.left.val >= node.val or node.left.val <= min_v:
                return False
        
        if node.right!= None:
            if node.right.val <= node.val or node.right.val >= max_v:
                return False
        
        return self.is_val(node.left, min_v, node.val) and self.is_val(node.right, node.val, max_v)  

    def inorder(self, root: TreeNode, res: []): 
        if root:
            self.inorder(root.left, res)
            res.append(root.val) 
            self.inorder(root.right, res)
# @lc code=end

