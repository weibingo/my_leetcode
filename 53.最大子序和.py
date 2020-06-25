#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = nums[:]
        dps = nums[0]
        dm = nums[0]
        for i in range(1, len(nums)):
            # dp[i] = max(dp[i-1]+nums[i], nums[i])
            # dm = max(dm, dp[i])
            if (dps > 0):
                dps = dps + nums[i]
                dm = max(dm, dps)
            else:
                dps = nums[i]
                dm = max(dm, dps)
        return dm
# @lc code=end

