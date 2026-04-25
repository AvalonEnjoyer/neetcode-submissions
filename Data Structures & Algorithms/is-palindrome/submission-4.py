class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = -1
        while i < len(s) and i<=len(s)+j:
            if not s[i].isalnum():
                i=i+1
                continue
            elif not s[j].isalnum():
                j = j-1
                continue
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i = i+1
                j = j-1
        return True