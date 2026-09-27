class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # for there to be a square, there must be 4 equal numbers when added up. 
        if len(matchsticks)<4:
            return False # square needs at least 4 sides
        # since sticks cannot be broken up, average length must be divisible by 4
        if sum(matchsticks)%4:
            return False
        target_side_length = sum(matchsticks)//4
        matchsticks.sort(reverse=True)
        n = len(matchsticks)
        sides = [0]*4

        # check if any of the possible 4 sums add up to target_side_length

        def backtrack(idx):
            if idx == n:
                return True

            for side in range(4):
                if sides[side] + matchsticks[idx] <= target_side_length:
                    sides[side] += matchsticks[idx]
                    if backtrack(idx+1):
                        return True
                    sides[side]-=matchsticks[idx]
                if sides[side] == 0:
                    break
            return False

        return backtrack(0)  
        