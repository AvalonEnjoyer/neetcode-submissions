class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(cur, mask):
            if len(cur) == n:
                res.append(cur.copy())
                return 
            for i in range(n):
                if not (mask & (1<<i)):
                    cur.append(nums[i])
                    backtrack(cur, mask | 1<<i)
                    cur.pop()
        
        backtrack([],0)
        return res