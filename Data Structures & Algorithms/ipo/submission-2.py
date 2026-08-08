class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        min_heap = []
        running_capital = w
        
        for index, profit in enumerate(profits):
            if capital[index] <= running_capital:
                heapq.heappush_max(max_heap, (profit, index))
            else:
                heapq.heappush(min_heap, (capital[index], index))
        
        print(max_heap, min_heap)
        while k>0:
            while min_heap and capital[min_heap[0][1]]<=running_capital:
                to_append_idx = heapq.heappop(min_heap)[1]
                heapq.heappush_max(max_heap, (profits[to_append_idx],to_append_idx))

            if not max_heap:
                break
            cur = heapq.heappop_max(max_heap)
            running_capital += cur[0]

            k-=1
        return running_capital
