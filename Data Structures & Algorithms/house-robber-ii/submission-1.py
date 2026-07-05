class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)

        def helper(numbers):
            rob1, rob2 = 0,0

            for num in numbers:
                temp = max(rob1+num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2


        return max(helper(nums[:-1]), helper(nums[1:]))