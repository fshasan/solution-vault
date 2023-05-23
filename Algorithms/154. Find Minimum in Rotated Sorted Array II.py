class Solution(object):
    def findMin(self, nums):
        final_lst = []
        for i in range(len(nums)):
            if nums[i] not in final_lst:
                final_lst.append(nums[i])
        
        final_lst = sorted(final_lst)
        return final_lst[0]