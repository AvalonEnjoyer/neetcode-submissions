class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        lengths = [a,b,c]
        lengths = [length for length in lengths if length>0]
        if len(lengths) <= 1:
            return ""

        chars = [[a,"a"],[b,"b"],[c,"c"]]
        heapq.heapify_max(chars)

        one, two = None, None
        prev = None
        res = [""]*(a+b+c)
        print(f"Length of final string {len(res)}")

        i = 0
        while chars and i<(a+b+c):
            cur = heapq.heappop_max(chars)
            if cur[1]==one and cur[1]==two:
                if not chars:
                    return "".join(res)
                prev = cur
                cur = heapq.heappop_max(chars)
                heapq.heappush_max(chars, prev)
            
            print(res)
            res[i]=cur[1]
            two = one
            one = cur[1]
            cur[0]-=1
            
            heapq.heappush_max(chars,cur)

            if chars[-1][0]==0:
                chars.pop()
            i+=1 

        print(len(res), res)
        return "".join(res)