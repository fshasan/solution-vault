class Solution(object):
    def removeElement(self, nums, val):
        while(True):
            if val not in nums:
                break
            else:
                nums.remove(val)

        return len(nums)