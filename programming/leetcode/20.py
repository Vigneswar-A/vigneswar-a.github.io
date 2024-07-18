class Solution:
    def isValid(self, s: str) -> bool:
        
        closemap = {'(':')', '{':'}', '[':']'}
        
        stack = []
        
        for c in s:
            if c in closemap:
                stack.append(c)
            elif not stack:
                return False
            elif closemap[stack.pop()] != c:
                return False
            
        return not bool(stack)