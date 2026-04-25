class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if nums is None:
            return []
        n = len(nums)
        if n<=2:
            return list(set(nums))
        nums.sort()
        nums_n = []
        count = 1
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                count += 1
            else:
                if count > n // 3:
                    nums_n.append(nums[i-1])
                count = 1
            if len(nums_n) > 2:
                return nums_n
        if count > n // 3:
            nums_n.append(nums[-1])
        return nums_n