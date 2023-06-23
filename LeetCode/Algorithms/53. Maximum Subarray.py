class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            global_max = nums[0]
            local_max = global_max
            for i in range(1, len(nums)):
                local_max = max(nums[i] + local_max, nums[i])
                global_max = max(local_max, global_max)

            return global_max