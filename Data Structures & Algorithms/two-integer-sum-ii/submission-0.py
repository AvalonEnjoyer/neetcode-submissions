class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum_map = {}
        for index, number in enumerate(numbers):
            complement = target - number
            if number not in sum_map:
                sum_map[complement] = index+1
                print(sum_map)
            elif numbers[sum_map[number]-1] == number:
                continue
            else:
                return [sum_map[number], index+1]