class Solution(object):
    def majorityElement(self, nums):
        dict = {}
        ans_lst = []
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        
        appear = len(nums) // 3
        for key, value in dict.items():
            if value > appear:
                ans_lst.append(key)

        return ans_lst