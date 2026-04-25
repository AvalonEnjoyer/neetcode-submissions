class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        last_min = float('inf')
        max_profit = 0
        for i in range(0, len(prices)):
            if prices[i] < last_min:
                last_min = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - last_min)
        return max_profit