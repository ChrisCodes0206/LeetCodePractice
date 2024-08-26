# Valid Anagram

class Solution(object):
    # Time: O(n) Space: O(n)
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmapS = {}
        hashmapT = {}
        
        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)

        for l in s: 
            if hashmapS[l] != hashmapT.get(l, 0):
                return False
        
        return True
 



s = "car"
t = "cat"
solution = Solution()
print(solution.isAnagram(s, t))