class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.lower()
        list = []
        for i in a:
            if ( ord(i) >= ord('a') ) and (ord(i) <= ord('z')) or ( ord(i) >= ord('A') ) and (ord(i) <= ord('Z')) or ((ord(i) >= ord('0') ) and (ord(i) <= ord('9'))):
                list.append(i)
        if list == list[::-1]:
            return True
        return False