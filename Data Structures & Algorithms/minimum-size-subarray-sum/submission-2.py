class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None:
            return 0
        minimum = 0
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
                minimum = right-left+1 if minimum==0 else min(minimum, right-left+1)
            right += 1
        return minimum