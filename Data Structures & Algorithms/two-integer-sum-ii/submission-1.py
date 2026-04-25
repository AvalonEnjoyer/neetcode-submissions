class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target and numbers[i] != numbers[j]:
                return [i+1, j+1]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1

