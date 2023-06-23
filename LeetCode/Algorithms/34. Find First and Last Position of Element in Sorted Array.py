class Solution(object):
    def searchRange(self, nums, target):
        first, last = -1, -1
        start = 0
        end = len(nums) - 1

        while(start <= end):
            if first != -1 and last != -1:
                break
            else:
                if nums[start] == target:
                    first = start
                else:
                    start += 1
                if nums[end] == target:
                    last = end
                else:
                    end -= 1
                
        return [first, last]