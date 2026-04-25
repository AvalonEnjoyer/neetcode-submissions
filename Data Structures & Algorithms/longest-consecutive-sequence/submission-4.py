class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        sequence_lengths = []
        current_longest = 1
        if len(nums) == 0:
            return 0
        for i, num in enumerate(nums):
            if i != 0:
                if num == last_num:
                    continue
                elif num - last_num == 1:
                    current_longest += 1
                else:
                    sequence_lengths.append(current_longest)
                    current_longest = 1
            last_num = num
        sequence_lengths.append(current_longest)
        return max(sequence_lengths)