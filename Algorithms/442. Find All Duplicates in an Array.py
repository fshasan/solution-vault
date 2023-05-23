class Solution(object):
    def findDuplicates(self, nums):
        dict = {}
        ans_lst = []
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        for key, value in dict.items():
            if value == 2:
                ans_lst.append(key)

        return ans_lst