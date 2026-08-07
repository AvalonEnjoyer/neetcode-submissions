class MedianFinder:

    def __init__(self):
        self._min_heap = []
        self._max_heap = []

    def addNum(self, num: int) -> None:
        if not self._min_heap or num > self._min_heap[0]:
            heapq.heappush(self._min_heap, num)
        else:
            heapq.heappush_max(self._max_heap, num)

        if len(self._min_heap)>len(self._max_heap)+1:
            temp = heapq.heappop(self._min_heap)
            heapq.heappush_max(self._max_heap, temp)
        elif len(self._max_heap)>len(self._min_heap)+1:
            temp = heapq.heappop_max(self._max_heap)
            heapq.heappush(self._min_heap, temp)
            
    def findMedian(self) -> float:
        if len(self._min_heap) == len(self._max_heap):
            return (self._min_heap[0]+self._max_heap[0])/2
        elif len(self._min_heap) > len(self._max_heap):
            return self._min_heap[0]
        else:
            return self._max_heap[0]