class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        last_min = float('inf')
        max_profit = 0
        for i in range(0, len(prices)):
            last_min = min(last_min, prices[i])
            max_profit = max(max_profit, prices[i] - last_min)
        return max_profit