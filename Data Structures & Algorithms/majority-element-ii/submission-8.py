class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if nums is None:
            return []
        n = len(nums)
        if n <= 2:
            return list(set(nums))
        candidate1, candidate2 = 0,0
        count_1, count_2 = 0, 0
        res = []
        for i in range(0, n):
            if candidate1 == nums[i]:
                count_1 += 1
            elif candidate2 == nums[i]:
                count_2 += 1
            elif count_1 == 0:
                candidate1 = nums[i]
                count_1 = 1
            elif count_2 == 0:
                candidate2 = nums[i]
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        count_1, count_2 = 0,0
        print(candidate1, candidate2)
        for i in range(0, n):
            if candidate1 == nums[i]:
                count_1 += 1
            elif candidate2 == nums[i]:
                count_2 += 1
        if count_1>n//3:
            res.append(candidate1)
        if count_2>n//3:
            res.append(candidate2)
        return res