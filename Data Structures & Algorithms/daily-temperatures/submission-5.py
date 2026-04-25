class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        for i in range(n-2, -1, -1):
            j = i+1
            while j<n and temperatures[j]<=temperatures[i]:
                if res[j] == 0: # Checking the res value for temp[j] to see if a greater element exists
                    j = n 
                    break 
                j += res[j] # jumping to the last value that was greater that temp[j]
            if j<n:
                res[i]=j-i
        return res