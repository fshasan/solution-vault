class Solution(object):
    def findDuplicate(self, nums):
        dict = {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1 
                
        for key, value in dict.items():
            if value > 1:
                ans = key
                break

        return ans