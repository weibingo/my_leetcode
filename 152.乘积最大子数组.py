#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, mx, mi = nums[0], nums[:], nums[:]
        for i in range(1, len(nums)):
            tmx = mx[i-1] * nums[i]
            tmi = mi[i-1] * nums[i]
            mx[i] = max(nums[i], tmx, tmi)
            mi[i] = min(nums[i], tmx, tmi)
            res = max(mx[i], res)
        return res
    
# @lc code=end

