class Solution(object):
    def singleNumber(self, nums):
        f = 0
        freq = {}
        for i in nums:
            if (i in freq):
                freq[i] += 1
            else:
                freq[i] = 1
                
        for key, value in freq.items():
            if value == 1:
                f = 1
                found = key
                break
                
        if f == 1:
            return found