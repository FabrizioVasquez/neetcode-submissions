class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lower_case_letter = [0] * 26
        for i in range(len(s)):
            lower_case_letter[ord(s[i])-ord('a')] +=1
            lower_case_letter[ord(t[i])-ord('a')] -=1
        for total in lower_case_letter:
            if total != 0:
                return False
        return True