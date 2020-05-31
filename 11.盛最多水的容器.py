#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max_area = 0
        tmp = 0
        while l < r:
            tmp = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, tmp)
            if height[l] > height[r]:
                r=r-1
            else:
                l=l+1
        return max_area
# @lc code=end

