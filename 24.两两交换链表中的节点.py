#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        t = head
        tt = None
        if (t is None or t.next is None):
            return t
        head = t.next
        while (t is not None and t.next is not None):
            p = t.next
            t.next = p.next
            p.next = t
            if (tt is not None):
                tt.next = p
            tt = t
            t = t.next
        return head

# @lc code=end

