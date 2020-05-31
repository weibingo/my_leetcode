#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n == 0):
            return 1
        elif (n == -1):
            return 1/x
        half = self.myPow(x, n//2)
        if (n % 2 == 0):
            return half * half
        else:
            return half * half * x

# @lc code=end

