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
        
        loc, load = 0, 0
        carrying = [] # curr => min_heap to track destination
        idx = 0

        while load<=capacity:
            if loc==trips[-1][-1] and load == 0:
                return True

            while carrying and trips[carrying[0].idx][2]==loc:
                cur = heapq.heappop(carrying)
                load-=trips[cur.idx][0]
                # print(f"Load after completing trip:{load}")

            if idx<len(trips):
                if trips[idx][1]==loc:
                    heapq.heappush(carrying, Locator(idx))
                    load+=trips[idx][0]
                    idx+=1
                else:
                    loc = trips[idx][1] if not carrying else min(trips[carrying[0].idx][2], trips[idx][1])
            else:
                loc = trips[carrying[0].idx][2] if carrying else trips[-1][-1]



        return False