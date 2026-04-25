class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]
        for i in range(n-2, -1, -1):
            j = i+1
            while j<n and temperatures[j]<=temperatures[i]:
                if res[n-1-j] == 0: # Checking the res value for temp[j] to see if a greater element exists
                    j = n 
                    break 
                j += res[n-1-j] # jumping to the last value that was greater that temp[j]
            if j<n:
                res.append(j-i)
            else:
                res.append(0)
        res.reverse()
        return res