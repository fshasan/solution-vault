class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        else:
            first = 1
            second = 2
            for i in range(3, n+1):
                res = first + second
                first = second
                second = res
            return res