# Score of Parentheses

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0

        for p in s:
            if (p == '('):
                stack.append(result)
                result = 0
            else:
                result = stack.pop() + max(result*2, 1)

        return result

solution = Solution()
print(solution.scoreOfParentheses("()"))


# 2 * (1 + (2 * 1))