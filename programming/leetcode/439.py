class Solution:
    def parseTernary(self, expression: str) -> str:
        
        stack = []
        for c in expression[::-1]:
            if stack and stack[-1] == '?': # c is the condition
                stack.pop() # remove the ?   
                x, y = stack.pop(), stack.pop() 
                stack.append(x if c == 'T' else y)
            elif c != ':':
                stack.append(c)
            
        return stack[0]

            
        