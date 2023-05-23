class Solution(object):
    def removeStars(self, s):
        lst = []
        for i in range(len(s)):
            if s[i] == "*":
                lst.pop(-1)
            else:
                lst.append(s[i])
        
        res = ''.join(lst)
        return res