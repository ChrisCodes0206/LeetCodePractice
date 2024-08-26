# Merge Sorted Array

class Solution(object):
    # Time: O(n) Space: O(1)
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n - 1
        while m > 0 and n > 0: 
            if nums2[n-1] > nums1[m-1]:
                nums1[tail] = nums2[n-1]
                n -= 1
            else:
                nums1[tail] = nums1[m-1]
                m -= 1
            tail -= 1

        while n > 0:
                nums1[tail] = nums2[n-1]
                n -= 1
                tail -= 1

        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution = Solution()
print(solution.merge(nums1, m, nums2, n))