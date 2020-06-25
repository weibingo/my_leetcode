#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return
        i, k = 1, -1
        while i<len(nums):
            if (nums[i] != nums[i-1]):
                if (k != -1):
                    nums[k] = nums[i]
                    k = k+1
            else:
                if (k == -1):
                    k = i
            i= i+1
        if (k != -1):
            del nums[k:len(nums)]
# @lc code=end

