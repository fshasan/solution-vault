class Solution(object):
    def removeTrailingZeros(self, num):
        for i in range(len(num)):
            if num[len(num)-i-1] != "0":
                return num[:(len(num)-i-1)+1]
                
