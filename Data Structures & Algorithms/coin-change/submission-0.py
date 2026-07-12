class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        change = {}
        # n=len(coins)
        # j = n-1
        # while j>=0:
        #     if coins[j]<=amount:
        #         break
        #     j-=1
        # if j==-1:
        #     return -1

        def dfs(amt):
            if amt == 0:
                return 0
            res = float('inf')
            for coin in coins:
                if amt-coin>=0:
                    if amt-coin not in change:
                        change[amt-coin] = 1+dfs(amt-coin)
                    res = min(res, change[amt-coin])
                        
            return res

        ans = dfs(amount)
        return -1 if ans == float('inf') else ans
        