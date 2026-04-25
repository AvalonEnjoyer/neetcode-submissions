class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for c in asteroids: # if left comes after right - collision happens
            alive = True
            if stack and ((stack[-1]>0) and (c<0)):
                while stack and (stack[-1]>0) and (c<0) and alive:
                    if abs(stack[-1])==abs(c):
                        alive = False
                        stack.pop()
                    elif abs(stack[-1])>abs(c):
                        alive = False
                    else:
                        stack.pop()
                if alive:
                    stack.append(c)
            else: 
                stack.append(c)
        return stack