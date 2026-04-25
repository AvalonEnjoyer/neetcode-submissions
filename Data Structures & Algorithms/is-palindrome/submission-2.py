class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = -1
        while i < len(s)//2:
            if not s[i].isalnum():
                i=i+1
                continue
            elif not s[j].isalnum():
                j = j-1
                continue
            else:
                if s[i] != s[j]:
                    return False
                i = i+1
                j = j-1
        return True