class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        else:
            f = 1
            while n > 1:
                if n % 4 != 0:
                    f = 0
                    break
                else:
                    n = n // 4

            if f == 0:
                return False
            else:
                return True