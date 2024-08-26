# Backspace String Compare

class Solution(object):
    # my solution
    # Time: O(n) Space: O(n)
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stackS = []
        stackT = []
        for l in s:
            if (l != '#'):
                stackS.append(l)
            elif(stackS):
                stackS.pop()


        for l in t:
            if (l != '#'):
                stackT.append(l)
            elif(stackT):
                stackT.pop()

        if (stackS == stackT): 
            return True
        else: 
            return False
        
    # optimized
    # Time: O(n) Space: O(1)
    def optimizedBackspaceCompare(self, s: str, t: str) -> bool:
        def nextValidChar(string, index):
            backspace = 0
            while index >= 0:
                if (backspace == 0 and string[index] != '#'):
                    break
                elif (string[index] == '#'):
                    backspace += 1
                else: 
                    backspace -= 1
                index -= 1
            return index
        
        indexS, indexT = len(s) - 1, len(t) - 1
        while indexS >= 0 or indexT >= 0: 
            indexS = nextValidChar(s, indexS)
            indexT = nextValidChar(t, indexT)

            charS = s[indexS] if indexS >= 0 else ""
            charT = t[indexT] if indexT >= 0 else ""

            if charS != charT:
                return False
            indexS -= 1
            indexT -= 1

        return True


solution = Solution()
print(solution.optimizedBackspaceCompare("ab#c", "b#c"))