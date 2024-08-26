# Number of Good Pairs

class Solution(object):
    # Time: O(n) Space: O(n)
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs = 0
        valid = {}
        for i in range(len(nums)):
            if nums[i] in valid:
                valid[nums[i]].append(i)
            else:
                valid[nums[i]] = [i]

        for value in valid.values():
            size = len(value)
            if (size >= 2):
                pairs += int((size * (size - 1)) / 2)

        return pairs
            

nums = [1,2,3]
solution = Solution()
print(solution.numIdenticalPairs(nums))