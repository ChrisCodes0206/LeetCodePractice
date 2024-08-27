#27 - Remove Element

class Solution(object):
    # Time: O(n) Space: O(1)
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        head = 0
        tail = len(nums)-1
        k = len(nums)

        while head < tail:
            if nums[tail] == val:
                nums[tail] = None
                tail -= 1
                k -= 1

            if nums[head] == val:
                nums[head] = nums[tail]
                nums[tail] = None
                tail -= 1
                k -= 1
            else:
                head += 1

        if len(nums) > 0 and nums[head] == val:
            nums[head] == None
            k -= 1
            
        return k