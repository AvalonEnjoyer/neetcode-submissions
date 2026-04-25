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
        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                count += 1
            else:
                if count > n//3:
                    nums_n.append(nums[i])
                count = 1
            if len(nums_n) == 2:
                return nums_n
        if count > n//3:
            nums_n.append(nums[i])
        return nums_n