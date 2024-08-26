# Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for parentheses in s:
            if (parentheses in valid):
                stack.append(parentheses)
            elif (stack and valid[stack[-1]] == parentheses):
                stack.pop()
            else: 
                return False

        if (not stack):
            return True


solution = Solution()
print(solution.isValid(")"))