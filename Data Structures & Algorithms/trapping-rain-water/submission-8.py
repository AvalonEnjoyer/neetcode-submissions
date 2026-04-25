class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        boundary_j = height[j]
        boundary_i = height[i]
        area = 0
        temp_count = 0
        while i < j:
            if boundary_i > boundary_j:
                j-=1
                if height[j] < boundary_j:
                    temp_count += 1
                    area += boundary_j - height[j]
                if height[j] >= boundary_j:
                    temp_count = 0
                    boundary_j = height[j]
            else:
                i += 1
                if height[i] < boundary_i:
                    temp_count += 1
                    area += boundary_i - height[i]
                if height[i] >= boundary_i:
                    temp_count = 0
                    boundary_i = height[i]
            if i >= j:
                boundary_difference = boundary_j-boundary_i if boundary_j>boundary_i else boundary_i-boundary_j
                area -= temp_count * boundary_difference
        return area