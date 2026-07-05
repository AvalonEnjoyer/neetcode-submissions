class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        cache = [-1]*n

        def calc(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(calc(i+1), calc(i+2))
            return cache[i]

        return min(calc(0), calc(1))