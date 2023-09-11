class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = [x for x in str(x)]
        flag = 1
        if len(x) % 2 == 1:
            mid = (len(x) // 2) + 1
        else:
            mid = len(x) // 2
        for i in range(0, mid):
            if x[i] != x[len(x) - 1 - i]:
                return False
        return True