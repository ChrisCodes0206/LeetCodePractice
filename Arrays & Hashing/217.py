# Contains Duplicate

class Solution(object):
    # Time: O(n) Space: O(n)
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


            
        
nums = [1,1,1,3,3,4,3,2,4,2]
solution = Solution()
print(solution.containsDuplicate(nums))