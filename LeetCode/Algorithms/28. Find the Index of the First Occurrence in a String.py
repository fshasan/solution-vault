class Solution(object):
    def strStr(self, haystack, needle):
        flag = 0
        i = 0
        while i < len(haystack):
            if needle == haystack[i : i + len(needle)]:
                flag = 1
                break
            else:
                i += 1

        if flag == 1:
            return i
        else:
            return -1
