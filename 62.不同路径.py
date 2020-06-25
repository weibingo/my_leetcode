#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if (m == 1):
            return 1
        if (n == 1):
            return 1
        dp = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[n-1]
        # return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
# @lc code=end

