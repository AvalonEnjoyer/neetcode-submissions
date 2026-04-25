class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            j = i + 1
            k = length - 1
            # if nums[i] == nums[j]:
            #     continue
            # else:
            while j < k:
                print(nums[i], nums[j], nums[k])
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k = k - 1
                elif s < 0:
                    j = j + 1
                else:
                    if [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    k -=1
        return result