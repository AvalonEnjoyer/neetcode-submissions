class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # for there to be a square, there must be 4 equal numbers when added up. 
        if len(matchsticks)<4:
            return False # square needs at least 4 sides
        # since sticks cannot be broken up, average length must be divisible by 4
        if sum(matchsticks)%4:
            return False
        
        target_side_length = sum(matchsticks)//4
        if max(matchsticks)>target_side_length:
            return False

        matchsticks.sort(reverse=True)
        n = len(matchsticks)
        dp = [float("-inf")]*(1<<n)

        def backtrack(mask):
            if mask == 0:
                return 0
            if dp[mask] != float("-inf"):
                return dp[mask]
            for i in range(n):
                if mask&(1<<i):
                    res = backtrack(mask^(1<<i))
                    if res >= 0 and (res + matchsticks[i] <= target_side_length):
                        dp[mask] = (res+matchsticks[i])%target_side_length
                        return dp[mask]
                    if mask == (1<<n)-1:
                        dp[mask] = -1
                        return -1
            dp[mask] = -1
            return -1
                    
        return not backtrack((1<<n)-1)  
        