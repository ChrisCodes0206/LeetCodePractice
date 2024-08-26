# Intersection of Two Arrays

class Solution(object):
    # Time: O(n + m) Space: O(n)
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        output = set()
        for n in nums1:
            hashmap[n] = 0

        for n in nums2:
            if n in hashmap:
                output.add(n)

        return list(output)


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

solution = Solution()
print(solution.intersection(nums1, nums2))