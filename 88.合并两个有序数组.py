#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if (n == 0):
            return nums1
        i, j = m-1, n-1
        k = len(nums1) -1
        while(k >= 0):
            if (i >= 0 and j >= 0):
                if (nums1[i] >= nums2[j]):
                    nums1[k] = nums1[i]
                    i = i-1
                else:    
                    nums1[k] = nums2[j]
                    j = j-1
            else:
                if (i >= 0):
                    nums1[k] = nums1[i]
                    i = i-1
                if (j >= 0):
                    nums1[k] = nums2[j]
                    j = j-1
            k = k -1

# @lc code=end

