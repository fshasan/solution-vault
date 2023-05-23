class Solution(object):
    def isPalindrome(self, s):
        s1 = ""
        for i in range(len(s)):
            if (
                (ord(s[i]) >= 48 and ord(s[i]) <= 57)
                or (ord(s[i]) >= 65 and ord(s[i]) <= 90)
                or (ord(s[i]) >= 97 and ord(s[i]) <= 122)
            ):
                s1 += s[i]

        if s1.lower() == s1[::-1].lower():
            return True
        else:
            return False
