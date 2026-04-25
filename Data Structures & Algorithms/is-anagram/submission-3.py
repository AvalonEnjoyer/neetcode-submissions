class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = False
        if len(s) != len(t):
            return is_anagram
        s_chars_count={}
        for char in s:
            if char in s_chars_count:
                s_chars_count[char] = s_chars_count[char]+1
            else:
                s_chars_count[char] = 1
        t_chars_count={}
        for char in t:
            if char not in s:
                return is_anagram
            else:
                if char not in t_chars_count:
                    t_chars_count[char] = 1
                else:
                    t_chars_count[char] = t_chars_count[char]+1
                    if s_chars_count[char] < t_chars_count[char]:
                        return is_anagram
        is_anagram = True
        return is_anagram