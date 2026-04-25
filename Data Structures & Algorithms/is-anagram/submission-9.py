class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars_count={}
        for char in s:
            s_chars_count[char] = s_chars_count.get(char, 0) + 1
        for char in t:
            if char not in s_chars_count:
                return False
            if s_chars_count[char] == 0:
                return False
            s_chars_count[char] -= 1
        return True