#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (nums is None or len(nums) == 0):
            return [-1, -1]
        start, end = 0, len(nums)-1
        return self.search(nums, target, start, end)
        # rmin, rmax = -1, -1
        # while(start <= end):
        #     mid = start + (end -start) //2
        #     if (nums[mid]==target):
        #         if (nums[start] < target):
        #             start = start =1
        #         else:
        #             rmin = start
        #         if (nums[end] > target):
        #             end = end -1
        #         else:
        #             rmax = end
        #         # rmin = mid
        #         # rmax = mid
        #         # left = mid -1
        #         # right = mid + 1
        #         # while(nums[left] == target and start <= left):
        #         #     rmin = left
        #         #     left = left -1
        #         # while(nums[right] == target and right <= end):
        #         #     rmax = right
        #         #     right = right + 1
        #     elif (nums[mid] < target):
        #         start = mid +1
        #     else:
        #         end = mid -1
        # return [rmin, rmax]

    def search(self, nums: List[int], target: int, start: int, end: int) -> List[int]:
        if (nums[start] == target and nums[end] == target):
            return [start, end]
        if (nums[start] > target or nums[end] < target):
            return [-1, -1]
        mid = start + (end -start) //2
        l = self.search(nums, target, start, mid)
        r = self.search(nums, target, mid+1, end)
        if l == [-1, -1]: return r
        if r == [-1, -1]: return l
        return [l[0], r[1]]
# @lc code=end

