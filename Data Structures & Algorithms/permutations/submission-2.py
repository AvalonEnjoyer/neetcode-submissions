class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(array, idx):
            if idx == n:
                res.append(array.copy())
                return 
            for i in range(idx,n):
                array[idx], array[i] = array[i], array[idx]
                backtrack(array, idx+1)
                array[i], array[idx] = array[idx], array[i]
        
        backtrack(nums, 0)
        return res