class Solution(object):
    def lengthOfLastWord(self, s):
        stack = []
        for i in s[::-1]:
            if i != " " and len(stack) >= 0:
                stack.append(i) 
            elif i == " " and len(stack) >= 1:
                return len(stack)

        return len(stack)
