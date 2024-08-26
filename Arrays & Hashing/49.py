# Group Anagrams
from collections import defaultdict
class Solution(object):
    # m: length of word, n: number of words
    # Time: O(n * m log m) Space: O(n * m)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        output = []
        
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in hashmap:
                hashmap[sortedWord].append(word)
            else: 
                hashmap[sortedWord] = [word]

        for value in hashmap.values():
            output.append(value)
            
        return output

    # Time: O(n * m) Space: O(n * m)
    def optimizedGroupAnagrams(self, strs):
        hashmap = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1

            hashmap[tuple(count)].append(word)

        return hashmap.values()


strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams(strs))