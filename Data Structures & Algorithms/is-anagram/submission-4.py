class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) < 1 and len(t) < 1) or len(s) != len(t):
            return False
        dicc1 = {}
        dicc2 = {}
        for i in range(len(s)):
            if not s[i] in dicc1:
                dicc1[s[i]] = 1
            else:
                dicc1[s[i]] += 1
            if not t[i] in dicc2:
                dicc2[t[i]] = 1
            else:
                dicc2[t[i]] += 1
        return dicc1 == dicc2
            