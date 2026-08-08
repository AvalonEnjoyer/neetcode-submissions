class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minimum = min(trips, key=lambda x:x[1])[1]
        maximum = max(trips, key=lambda x:x[2])[2]
        n = maximum-minimum+1
        pass_change = [0]*(n+1)

        for passengers, start, end in trips:
            pass_change[start-minimum] += passengers
            pass_change[end-minimum] -= passengers

        curr = 0
        for change in pass_change:
            curr += change
            if curr > capacity:
                return False

        return True