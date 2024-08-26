# Maximum Nesting Depth of the Parentheses

class Solution(object):
    # Time: O(n) Space: O(n)
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        nestCount = 0
        maxCount = 0
        for c in s:
            if c == '(':
                stack.append(c)
                nestCount += 1
                if nestCount > maxCount:
                    maxCount = nestCount
            elif (c == ')'):
                stack.pop()
                nestCount -= 1
        return maxCount

    # Time: O(n) Space: O(1)
    def optimizeMaxDepth(self, s):
        nestCount = 0
        maxCount = 0
        for i in range(len(s)):
            if (s[i] == '('):
                nestCount += 1
                if nestCount > maxCount:
                    maxCount = nestCount
            elif (s[i] == ')'):
                nestCount -= 1

        return maxCount
solution = Solution()

s = "8*((1*(5+6))*(8/6))"

# print(solution.maxDepth(s))

for c in range(len(s)):
    print(s[c])

print(solution.optimizeMaxDepth(s))
