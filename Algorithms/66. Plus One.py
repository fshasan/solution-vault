class Solution(object):
    def plusOne(self, digits):
        res = 0
        for i in range(len(digits)):
            num = digits[i] * (10 ** (len(digits) - i - 1))
            res += num

        res = res + 1
        fin_res = [int(x) for x in str(res)]

        return fin_res