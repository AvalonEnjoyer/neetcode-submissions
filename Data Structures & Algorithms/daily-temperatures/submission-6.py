class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i in range(n): # when unresolved element in less than current temp
            while stack and temperatures[stack[-1]]<temperatures[i]:
                prev = stack.pop() # index of unresolved element
                res[prev]=i-prev # update res from 0 to i-prev
            stack.append(i) # index of the latest element always goes into the stack
        return res