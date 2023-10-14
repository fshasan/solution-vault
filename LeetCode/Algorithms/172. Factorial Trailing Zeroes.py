class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        if n == 0:
            return 0
        fact_number = factorial(n)

        for i in str(fact_number)[::-1]:
            if i == '0':
                count += 1
            else:
                return count
                
    def factorial(n):
        if n < 0:
            return 
        elif n <= 1:
            return 1
        else:
            return n * factorial(n-1)
