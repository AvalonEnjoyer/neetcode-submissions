class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            print(f"Res: {res} bin: {bin(res)} | num: {num} bin: {bin(num)}")
            res |= num
        return res << (len(nums) - 1)