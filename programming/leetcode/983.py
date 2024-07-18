class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        i,j,n = 0,0,len(pushed)
        
        while i < n or stack:
            if stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()
            elif i < n:
                stack.append(pushed[i])
                i += 1                      
            else:
                return False
            
        return True
                    
        
            
        