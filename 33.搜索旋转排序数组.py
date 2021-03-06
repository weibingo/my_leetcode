#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) -1
        while (start <= end):
            mid = start + (end -start) // 2
            if (nums[mid] == target):
                return mid
            # 旋转点在右边
            if (nums[start] < nums[mid]):
                if (nums[mid] > target and nums[start] <= target):
                    end = mid - 1
                else:
                    start = mid + 1
            elif(nums[start] > nums[mid]):
                if (nums[mid] < target and nums[end] >= target):
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                # skip duplicate one
                start = start + 1
        return -1
    
# @lc code=end

