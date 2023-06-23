class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = low + (high - low) // 2

        while(low < high):     
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            mid = low + (high - low) // 2

        if target > nums[high]:
            return high + 1
        elif target < nums[low]:
            return low
        else:
            return low + (high - low) // 2