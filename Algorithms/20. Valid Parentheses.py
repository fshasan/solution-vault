class Solution(object):
    def isValid(self, s):
        if len(s) == 1:
            return False
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        else:
            stack = []
            f = 0
            for i in s:
                if i == "(" or i == "{" or i == "[":
                    stack.append(i)
                if (i == ")" or i == "}" or i == "]") and (len(stack) == 0):
                    return False
                else:
                    if i == ")":
                        f = 1
                        if f == 1 and stack[-1] == "(":
                            stack.pop(-1)
                        else:
                            return False
                    if i == "}":
                        f = 2
                        if f == 2 and stack[-1] == "{":
                            stack.pop(-1)
                        else:
                            return False
                    if i == "]":
                        f = 3
                        if f == 3 and stack[-1] == "[":
                            stack.pop(-1)
                        else:
                            return False

            if len(stack) == 0:
                return True
            else:
                return False
