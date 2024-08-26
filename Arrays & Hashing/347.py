# Top K Frequent Elements

class Solution(object):
    # Time: O(n) Space: O(n)
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for n in nums:
            frequency[n] = 1 + frequency.get(n, 0)
        
        for num in frequency:
            buckets[frequency[num]].append(num)

        count = 0
        output = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
            
        
nums = [1, 1, 1, 2, 2, 2, 3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))
