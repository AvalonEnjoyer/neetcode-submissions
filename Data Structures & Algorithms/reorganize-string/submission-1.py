class Solution:
    def reorganizeString(self, s: str) -> str:
        char_map = [[0,i] for i in range(26)]
        for char in s:
            char_map[ord(char)-ord("a")][0]+= 1
        char_map = [[chars[0],chars[1]] for chars in char_map if chars[0]>0]

        heapq.heapify_max(char_map)
        res = ""
        prev = None

        while char_map or prev:
            if prev and not char_map:
                return ""

            curr = heapq.heappop_max(char_map)
            res += chr(97+curr[1])
            curr[0]-=1
            
            if prev:
                heapq.heappush_max(char_map, prev)
                prev = None


            if curr[0] > 0:
                prev = curr

        return res
