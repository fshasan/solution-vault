class Solution(object):
    def search(self, nums, target):
        flag = 0
        low = 0
        high = len(nums) - 1
        
        while(low <= high):
            mid = (high - low) + low // 2
            if (target == nums[mid]):
                flag = 1
                break
            elif (target > nums[mid]):
                low = mid + 1
            else:
                high = mid - 1

        if flag == 1:
            return mid
        else:
            return -1