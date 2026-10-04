class Solution:
    def isValid(self, s: str) -> bool:
        dicc = {
            '(':')',
            '{':'}',
            '[':']'
        }
        general = []
        for i in range(len(s)):
            if s[i] in dicc.keys():
                general.append(s[i])
            
            if s[i] in dicc.values():
                if not general:
                    return False
                if dicc[general[-1]] == s[i]:
                    tmp = general.pop()
                else:
                    return False

        return len(general) == 0