#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while(start < end):
            mid = (end - start) // 2
            rs = guess(mid)
            if (rs == 0):
                return mid
            elif(rs == 1):
                end = mid -1
            else:
                start = mid + 1
        
# @lc code=end

