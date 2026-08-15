class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, temp, summa):
            if summa == target:
                res.append(temp.copy())
                return
            if summa>target or i>=n:
                return

            temp.append(candidates[i])
            backtrack(i+1, temp, summa+candidates[i])
            temp.pop()

            while i+1<n and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1, temp, summa)

        backtrack(0,[],0)
        return res
