class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.lower()
        j = len(s) - 1
        counter = 0
        for i in range(len(s)):
            if not a[i].isalnum():
                continue
            while not a[j].isalnum():
                j -= 1
            if a[j] != a[i]:
                return False
            print(a[i],a[j])
            j-=1
        return True