class Solution(object):
    def findPeakElement(self, nums):
        max_nums = sorted(nums)[-1]
        return nums.index(max_nums)