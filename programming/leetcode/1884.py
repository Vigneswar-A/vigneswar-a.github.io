class Solution:
    def minOperations(self, s: str) -> int:
        
        zero = '0'
        zmoves = 0
        
        one = '1'
        omoves = 0
        
        for c in s:
            if zero != c:
                zmoves += 1
            
            if one != c:
                omoves += 1
                
            zero = '0' if zero == '1' else '1'
            one = '1' if one == '0' else '0'
            
        return min(zmoves, omoves)
                    
        