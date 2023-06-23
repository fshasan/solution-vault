class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        for key, value in dict.items():
            if value > 1:
                return True

        return False
