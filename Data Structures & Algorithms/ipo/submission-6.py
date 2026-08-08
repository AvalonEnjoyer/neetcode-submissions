class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        indices = list(range(n))
        indices.sort(key=lambda x:capital[x])

        max_heap = []

        class Node():
            def __init__(self, idx):
                self.idx = idx
            
            def __lt__(self, other):
                if self.idx!=other.idx:
                    return profits[self.idx]<profits[other.idx]
                return self.idx<other.idx

        res = w
        idx = 0
        for _ in range(k):
            while idx<n and capital[indices[idx]]<=res:
                heapq.heappush_max(max_heap, Node(indices[idx]))
                idx+=1
            if not max_heap:
                return res
            res += profits[heapq.heappop_max(max_heap).idx]

        return res