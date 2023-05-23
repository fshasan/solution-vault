class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1
        else:
            return nums.index(target)