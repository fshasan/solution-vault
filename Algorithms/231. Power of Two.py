class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        else:
            f = 1
            while n > 1:
                if n % 2 != 0:
                    f = 0
                    break
                else:
                    n = n // 2

            if f == 0:
                return False
            else:
                return True