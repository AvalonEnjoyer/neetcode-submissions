class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0] * 3
        for num in nums:
            freq[num] += 1
        count = 0
        for i, freq in enumerate(freq):
            for j in range(freq):
                if nums[count] != i:
                    nums[count] = i
                count += 1
        