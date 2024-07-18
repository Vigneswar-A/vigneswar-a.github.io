class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        #edge cases
        if len(num) <= 2:
            return False     
        if int(num) == 0:
            return True
        
        #last index
        end_idx = len(num)
        res = False   
        def backtrack(num, prev, end):
            nonlocal res
            if res: #we already got the answer
                return None
            
            for i in range(1, len(num)+1):
                for j in range(i+1, len(num)+1):
                    
                    curr = int(num[:i])
                    nxt = int(num[i:j])
                    
                    if str(curr) != num[:i] or str(nxt) != num[i:j]: #not a valid number (0xxx)
                        continue

                    if prev + curr == nxt: 
                        if j == end: # all the indices are covered
                            res = True
                            return None
                        backtrack(num[i:], curr, end-i) 
                        
        for i in range(1, len(num)):
            if str(int(num[:i])) == num[:i]:
                backtrack(num[i:] , int(num[:i]), end_idx-i) #back tracking
            
        return res
                        
                        
            
                        
            
                    
                
                
        