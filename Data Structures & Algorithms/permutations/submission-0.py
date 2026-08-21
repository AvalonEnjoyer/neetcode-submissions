class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(cur, status):
            if len(cur) == n:
                res.append(cur.copy())
                return
            for i in range(n):
                if status[i] == False:
                    status[i] = True
                    cur.append(nums[i])
                    backtrack(cur, status)
                    cur.pop()
                    status[i]=False
            return res
            

        backtrack([],[False]*n)
        return res