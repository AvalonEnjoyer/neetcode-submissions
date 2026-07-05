class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)

        def helper(numbers):
            n = len(numbers)
            dp = [0]*n
            dp[0]=numbers[0]
            dp[1]=max(numbers[0], numbers[1])

            for i in range(2,n,1):
                dp[i] = max(numbers[i]+dp[i-2], dp[i-1]) 
    
            return dp[-1]

        return max(helper(nums[:-1]), helper(nums[1:]))