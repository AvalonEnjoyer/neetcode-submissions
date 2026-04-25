class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for c in asteroids: # if left comes after right - collision happens
            alive = True
            while stack and (stack[-1]>0) and (c<0) and alive:
                diff = stack[-1]+c
                if diff ==0:
                    alive = False
                    stack.pop()
                elif diff>0:
                    alive = False
                else:
                    stack.pop()
            if alive:
                stack.append(c)
        return stack