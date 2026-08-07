class Solution:
    def reorganizeString(self, s: str) -> str:
        char_map = [[0,i] for i in range(26)]
        for char in s:
            char_map[ord(char)-ord("a")][0]+= 1
        char_map = [[chars[0],chars[1]] for chars in char_map if chars[0]>0]

        heapq.heapify_max(char_map)
        res = []
        doghouse = None
        recent = 0
        while char_map or doghouse:
            if doghouse and not char_map:
                return ""

            curr = heapq.heappop_max(char_map)
            if doghouse:
                heapq.heappush_max(char_map, doghouse)
                doghouse = None

            if not res or curr[1]!=recent:
                recent = curr[1]
                res.append(chr(97+curr[1]))
                curr[0]-=1
                if curr[0] > 0:
                    heapq.heappush_max(char_map, curr)
            else:
                doghouse = curr
            

        return "".join(res)
