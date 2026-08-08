class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        counts = [a,b,c]
        chars = []
        for i,count in enumerate(counts):
            if count!=0:
                heapq.heappush_max(chars,[count,chr(ord("a")+i)])
        
        print(chars)

        while chars:
            cur = heapq.heappop_max(chars)
            if len(res)>1 and res[-1]==res[-2]==cur[1]:
                print(res)
                if not chars:
                    break
                temp = cur
                cur = heapq.heappop_max(chars)
                heapq.heappush_max(chars, temp)

                res+=cur[1]
                cur[0]-=1
                if cur[0]:
                    heapq.heappush_max(chars, cur)
                
            else:
                res+=cur[1]
                cur[0]-=1
                if cur[0]:
                    heapq.heappush_max(chars, cur)
        return res