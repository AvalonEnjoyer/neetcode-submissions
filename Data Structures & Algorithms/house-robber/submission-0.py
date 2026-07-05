class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n<3:
            return max(nums)
        
        memo = [-1]*n

        def calc(i):
            if i>=n:
                return 0
            if memo[i]!= -1:
                return memo[i]
            memo[i] = max(nums[i]+calc(i+2), calc(i+1))
            return memo[i]

        return calc(0)