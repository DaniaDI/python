class Solution(object):
    def isValid(self, s) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


sol = Solution()
print(sol.isValid("([])"))       
print(sol.isValid("([)]"))     
print(sol.isValid("()[]{}"))   