class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k = k - 1
                elif s < 0:
                    j = j + 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    k -=1
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
        return result