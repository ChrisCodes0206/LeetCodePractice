# Two Sum

class Solution(object):
    # Time: O(n) Space: O(n)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if (diff in hashmap):
                return [i, hashmap[diff]]
            hashmap[n] = i

nums = [3, 3]
target = 6
solution = Solution()
print(solution.twoSum(nums, target))