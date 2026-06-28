class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        num_map = [0]*(n**2)
        repeated = 0
        for i in range(n):
            for j in range(n):
                num_map[grid[i][j]-1] += 1
                if num_map[grid[i][j]-1] == 2:
                    repeated = grid[i][j]
                    
        return [repeated, num_map.index(0)+1]
