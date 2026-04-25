class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None:
            return 0
        minimum = 0
        n = len(nums)
        left = 0
        right = 0
        sum = 0
        while right < n:
            sum += nums[right]
            if sum >= target:
                while sum - nums[left] >= target:
                    sum -= nums[left]
                    left += 1
                minimum = right-left+1 if minimum==0 else min(minimum, right-left+1)
            right += 1
        return minimum