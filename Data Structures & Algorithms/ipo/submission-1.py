class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        temp = []
        running_capital = w
        
        for index, profit in enumerate(profits):
            if capital[index] <= w:
                heapq.heappush_max(max_heap, (profit, index))
            else:
                heapq.heappush_max(temp, (profit, index))
        
        while k>0:
            if not max_heap:
                break
            cur = heapq.heappop_max(max_heap)
            running_capital += profits[cur[1]]
            while temp:
                heapq.heappush_max(max_heap, heapq.heappop_max(temp))
            k-=1
        return running_capital
