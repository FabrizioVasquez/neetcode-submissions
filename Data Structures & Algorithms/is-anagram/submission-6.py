class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if (len(s) != len(t) or (len(s)<1 and len(t)<1)):
                return False
            if len(s) != len(t):
                return False

            contador = [0] * 26

            for i in range(len(s)):
                contador[ord(s[i]) - ord('a')] += 1
                contador[ord(t[i]) - ord('a')] -= 1

            return all(x == 0 for x in contador)