class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        num_map = [0]*(n**2)

        for i in range(n):
            for j in range(n):
                num_map[grid[i][j]-1] += 1
        
        return [num_map.index(2)+1, num_map.index(0)+1]
