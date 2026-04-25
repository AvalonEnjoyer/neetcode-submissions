class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        max_count = 0
        freq_map = {}
        while max_count <= n//2 and i < len(nums):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
            max_count = max(max_count, freq_map[nums[i]])
            i+=1
        for key, value in freq_map.items():
            if value == max_count:
                return key
        return None