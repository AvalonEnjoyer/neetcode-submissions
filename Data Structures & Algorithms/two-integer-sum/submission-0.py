class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter_1 = 0
        for first_num in nums:
            counter_2 = counter_1 + 1
            for second_num in nums[counter_1+1:]:
                if first_num + second_num == target:
                    return[counter_1, counter_2]
                counter_2 += 1
            counter_1 +=1
