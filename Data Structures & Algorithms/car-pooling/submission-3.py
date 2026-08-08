class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x:x[1])
        class Locator():
            def __init__(self, idx):
                self.idx=idx
            
            def __lt__(self, other):
                return trips[self.idx][2]<=trips[other.idx][2]

            def __str__(self):
                return self.idx
        
        load = 0
        carrying = [] # curr => min_heap to track destination
        
        for trip in trips:
            while carrying and trip[1]>= carrying[0][0]:
                load -= heapq.heappop(carrying)[1]

            load += trip[0]

            if load > capacity:
                return False
            
            heapq.heappush(carrying, (trip[2], trip[0]))

        return True