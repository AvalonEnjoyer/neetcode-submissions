import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[-1*(point[0]**2 + point[1]**2), point[0], point[1]] for point in points]
        heapq.heapify(points)

        while len(points)>k:
            heapq.heappop(points)
        
        res = []
        while points:
            d,x,y = heapq.heappop(points)
            res.append([x,y])

        return res
        