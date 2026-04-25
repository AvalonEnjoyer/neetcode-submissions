class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i<len(nums1) and j<len(nums2):
            m-=i
            if nums1[i] == 0 and i>=m:
                nums1[i] = nums2[j]
                j+=1
            elif nums1[i] > nums2[j]:
                k = len(nums1)-1
                while k > i:
                    nums1[k] = nums1[k-1]
                    k -= 1
                nums1[i] = nums2[j]
                j+=1
            i+=1