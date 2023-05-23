class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        s = ' '.join(s[::-1])
        return s