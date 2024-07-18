class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num += "0"
        removed = []
        stack = []
        for i in num:
            while len(removed) < k and stack and  i < stack[-1]:
                removed.append(stack.pop())
            stack.append(i)
            
        stack.pop()
    
        return ''.join(stack or "0").lstrip('0') or '0' #converted to int to remove leading zeros
            
        
            
        