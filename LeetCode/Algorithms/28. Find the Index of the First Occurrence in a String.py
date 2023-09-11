class Solution(object):
    def strStr(self, haystack, needle):
        flag = 0
        i = 0
        while i < len(haystack):
            if needle == haystack[i : i + len(needle)]:
                return i
            else:
                i += 1
        return -1
