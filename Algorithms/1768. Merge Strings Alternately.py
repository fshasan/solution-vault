class Solution(object):
    def mergeAlternately(self, word1, word2):
        f = 0
        res = ''
        if len(word1) > len(word2):
            length = len(word2)
            f = 1
        elif len(word1) < len(word2):
            length = len(word1)
            f = 2
        else:
            length = len(word1)

        for i in range(length):
            res += word1[i] + word2[i]
            
        if f == 1:
            res += word1[length:]
            return res
            
        elif f == 2:
            res += word2[length:]
            return res
            
        else:
            return res