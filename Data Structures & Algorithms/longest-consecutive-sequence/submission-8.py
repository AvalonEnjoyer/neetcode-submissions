# Solution 2 - 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums)==1:
            return 1
        nums.sort()
        max_length = 1
        current_longest = 1

        for i, num in enumerate(nums):
            if i != 0:
                if num == last_num:
                    continue
                elif num - last_num == 1:
                    if current_longest == 0:
                        current_longest = 1
                    current_longest += 1
                else:
                    if max_length < current_longest:
                        max_length = current_longest
                    current_longest = 1
            last_num = num
        return max_length if max_length > current_longest else current_longest

# # Solution 1 - 100% runtime and 100% memory
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums.sort()
#         sequence_lengths = []
#         current_longest = 1
#         if len(nums) == 0:
#             return 0
#         for i, num in enumerate(nums):
#             if i != 0:
#                 if num == last_num:
#                     continue
#                 elif num - last_num == 1:
#                     current_longest += 1
#                 else:
#                     sequence_lengths.append(current_longest)
#                     current_longest = 1
#             last_num = num
#         sequence_lengths.append(current_longest)
#         return max(sequence_lengths)