class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if nums is None:
            return []
        n = len(nums)
        candidate1, candidate2 = 0,0
        count_1, count_2 = 0, 0
        res = []
        for num in nums:
            if candidate1 == num:
                count_1 += 1
            elif candidate2 == num:
                count_2 += 1
            elif count_1 == 0:
                candidate1 = num
                count_1 = 1
            elif count_2 == 0:
                candidate2 = num
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        count_1, count_2 = 0,0
        for num in nums:
            if candidate1 == num:
                count_1 += 1
            elif candidate2 == num:
                count_2 += 1
        if count_1>n//3:
            res.append(candidate1)
        if count_2>n//3:
            res.append(candidate2)
        return res