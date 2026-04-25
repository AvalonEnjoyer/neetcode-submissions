class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1]*length
        prefix_product, suffix_product = 1, 1
        for i in range(length):
            products[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(length-1, -1, -1):
            products[i] *= suffix_product
            suffix_product *= nums[i]
            print(products)
        return products
            