class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(1,len(prices)):
            profit = prices[i]-prices[i-1] if prices[i]-prices[i-1] > 0 else 0
            if profit != 0:
                max_profit += profit
        return max_profit
