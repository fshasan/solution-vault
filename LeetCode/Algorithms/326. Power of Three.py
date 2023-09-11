class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        else:
            f = 1
            while n > 1:
                if n % 3 != 0:
                    return False
                else:
                    n = n // 3
            return True