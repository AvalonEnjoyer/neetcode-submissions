class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, n = [], len(nums)
        visited = [False]*n
        temp = []

        def dfs():
            if len(temp)==n:
                res.append(temp.copy())
                return
            for i in range(n):
                if visited[i]:
                    continue
                if i and nums[i]==nums[i-1] and visited[i-1]:
                    continue
                temp.append(nums[i])
                visited[i]=True
                dfs()
                visited[i]=False
                temp.pop()

        dfs()
        return res