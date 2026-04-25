class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        max_num = float('-inf')
        max_count = 0
        freq_map = {}
        while max_count <= n//2 and i < len(nums):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
            if freq_map[nums[i]] > max_count:
                max_num = nums[i]
                max_count = freq_map[nums[i]]
            i += 1
        print(freq_map)
        return max_num