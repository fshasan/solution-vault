class Solution(object):
    def addBinary(self, a, b):
        res = 0
        for i in range(len(a)):
            res += int(a[len(a)-i-1]) * (2 ** i)
            
        res1 = 0
        for i in range(len(b)):
            res1 += int(b[len(b)-i-1]) * (2 ** i)

        fin_res = res + res1
        if fin_res == 0:
            return "0"
        else:        
            bin_res = ''
            while(fin_res > 0):
                bin_res += str(fin_res % 2)
                fin_res = fin_res // 2

            return bin_res[::-1]