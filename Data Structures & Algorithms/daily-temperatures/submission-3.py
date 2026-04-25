class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]
        for i in range(n-2, -1, -1):
            j = i+1
            while j<n-1 and temperatures[j]<=temperatures[i]:
                j+=1
            if temperatures[j]>temperatures[i]:
                res.append(j-i)
            else:
                res.append(0)
        res.reverse()
        return res