class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1 - 100% Runtime and 100% Memory
        counter_1 = 0
        for first_num in nums:
            counter_2 = counter_1 + 1
            for second_num in nums[counter_1+1:]:
                if first_num + second_num == target:
                    return[counter_1, counter_2]
                counter_2 += 1
            counter_1 +=1
        
        # Solution 2 - 100% Runtime and 91.06% Memory 
        # complements = {}  # value -> index
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in complements:
        #         return [complements[complement], i]
        #     complements[num] = i

