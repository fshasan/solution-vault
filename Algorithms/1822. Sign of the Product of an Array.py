class Solution(object):
    def arraySign(self, nums):
        if 0 in nums:
            return 0
        else:
            count = 0
            for i in nums:
                if i < 0:
                    count += 1

            if count % 2 == 0:
                return 1
            else:
                return -1