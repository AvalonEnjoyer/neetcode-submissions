class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = 1
        cur_min = 1

        for num in nums:
            temp_max = cur_max*num
            cur_max = max(num, temp_max,cur_min*num)
            cur_min = min(num, temp_max,num*cur_min)
            res = max(res, cur_max)
        return res
