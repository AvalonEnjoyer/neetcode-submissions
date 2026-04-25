class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        complements = {}
        for j, num in enumerate(nums):
            if num in complements and j-complements[num] <= k:
                return True
            complements[num] = j
        return False