class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set(nums)

        if len(num_set) == len(nums):
            return False
        else:
            return True