class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        sum_ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(i != j):
                    sum_ans = nums[i] +  nums[j]
                    if(sum_ans == target):
                        return [i,j]
            