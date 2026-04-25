class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        import bisect 
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        print(nums)
        print(prefix)

        res = float('inf')
        for i in range(n):
            needed = prefix[i] + target
            j = bisect.bisect_left(prefix, needed)
            if j<=n:
                res=min(res,j-i)
        return 0 if res==float('inf') else res