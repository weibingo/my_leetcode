#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (head is None):
            return head
        p1, p2 = head, head
        while (p1 is not None):
            p2 = p1.next
            if (p2 is not None and p1.val == p2.val):
                p1.next = p2.next
            else:
                p1 = p1.next
        return head
# @lc code=end

