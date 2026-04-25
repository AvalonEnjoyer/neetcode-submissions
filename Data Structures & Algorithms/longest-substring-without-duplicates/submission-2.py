class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        char_map = [False]*95
        left=0
        right=0
        max_len=0

        while right<len(s):
            while char_map[ord(s[right])-ord("!")] == True:
                char_map[ord(s[left])-ord("!")] = False
                left+=1
            char_map[ord(s[right])-ord("!")] = True
            max_len = max(max_len, right-left+1)
            right+=1
        return max_len