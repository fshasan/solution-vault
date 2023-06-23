class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        ans = []
        total = 2
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for key, value in dict.items():
            if value == 1:
                ans.append(key)
                if len(ans) == total:
                    return ans
