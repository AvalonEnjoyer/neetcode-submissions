import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[point[0]**2 + point[1]**2, point[0], point[1]] for point in points]
        heapq.heapify(points)
        res = []

        while k>0:
            a_point = heapq.heappop(points)[1:]
            res.append(a_point)
            k-=1 
            
        return res
        