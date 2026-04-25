class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        boundary_j = 0
        boundary_i = 0
        area = 0
        while i < j:
            if height[i] < height[j]:
                if height[i] > boundary_i:
                    boundary_i = height[i]
                else:
                    area += boundary_i - height[i]
                i += 1
            else:
                if height[j] > boundary_j:
                    boundary_j = height[j]
                else:
                    area += boundary_j - height[j]
                j-=1
        return area