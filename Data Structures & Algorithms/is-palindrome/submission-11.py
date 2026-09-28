class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s
        j = len(s) - 1
        counter = 0

        for i in range(len(s)):
            if not a[i].isalnum():
                continue

            while not a[j].isalnum():
                j -= 1

            if ord(a[i]) >= ord('A') and ord(a[i]) <= ord('Z'):
                tmp = ord(a[i]) + 32
            else:
                tmp = ord(a[i])

            if ord(a[j]) >= ord('A') and ord(a[j]) <= ord('Z'):
                tmp2 = ord(a[j]) + 32
            else:
                tmp2 = ord(a[j])

            if tmp != tmp2:
                counter += 1
                print(a[i], a[j])
                print(counter)
                return False

            j -= 1

        return True