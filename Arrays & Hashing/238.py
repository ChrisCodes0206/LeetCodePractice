# Product of Array Except Self

class Solution(object):
    # Time: O(n) Space: O(n)
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [1] * len(nums)
        prefix = 1
        
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]

        postfix = 1
        
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]

        return products
    
nums = [1,2,3,4]
solution = Solution()
print(solution.productExceptSelf(nums))