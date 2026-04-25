class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for c in asteroids: # if empty stack or same polarity or left followed by right
            if not stack or (stack[-1]>0) == (c>0) or (stack[-1]<0) and (c>0):
                stack.append(c)
            else: # if left comes after right - collision happens
                while stack and (stack[-1]>0) and (c<0):
                    x = stack.pop()
                    if x+c == 0:
                        c = 0
                        break 
                    elif abs(x)>abs(c):
                        c = x
                if c!= 0:
                    stack.append(c)
        return stack