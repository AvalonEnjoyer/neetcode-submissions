class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        target_sum = sum(nums)//k
        if max(nums)>target_sum:
            return False
        n = len(nums)
        dp = [float("-inf")]*(1<<n)
        nums.sort(reverse=True)
        def dfs(mask):
            if mask == 0:
                return 0
            if dp[mask]!=float("-inf"):
                return dp[mask]
            
            for i in range(n):
                if mask & (1<<i):
                    res = dfs(mask^(1<<i))
                    if res >= 0 and (res+nums[i]<=target_sum):
                        dp[mask] = (res+nums[i])%target_sum
                        return dp[mask]
                    # if mask == (1<<n)-1:
                    #     dp[mask] = -1
                    #     return -1
            dp[mask] = -1
            return -1
        return dfs((1<<n)-1) == 0