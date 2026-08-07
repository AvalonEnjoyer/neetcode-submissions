class Solution:
    def reorganizeString(self, s: str) -> str:
        char_map = [0]*26
        for char in s:
            char_map[ord(char)-ord("a")]+= 1

        max_idx = char_map.index(max(char_map))
        max_freq = char_map[max_idx]

        if max_freq > (len(s)+1) // 2:
            return ""
        
        res = [""]*len(s)
        idx = 0 
        max_char = chr(max_idx+ord("a"))

        while char_map[max_idx]>0:
            res[idx]=max_char
            idx+=2
            char_map[max_idx]-=1

        for i in range(26):
            while char_map[i]>0:
                if idx >= len(s):
                    idx = 1
                res[idx]=chr(i+ord("a"))
                idx+=2
                char_map[i]-=1
        
        return "".join(res)

