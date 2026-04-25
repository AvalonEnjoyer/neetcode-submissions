class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float('inf')
        n = len(nums)
        left = 0
        right = 0
        window_sum = 0
        while right < n:
            window_sum += nums[right]
            if window_sum >= target:
                while window_sum - nums[left] >= target:
                    window_sum -= nums[left]
                    left += 1
                minimum = min(minimum, right-left+1)
            right += 1
        minimum = 0 if minimum == float('inf') else minimum
        return minimum