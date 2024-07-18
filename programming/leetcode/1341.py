class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        lc  = rc = 0
        
        for c in s:
            if c == 'L':
                lc += 1
            elif c == 'R':
                rc += 1
            
            if lc == rc:
                lc = 0
                rc = 0
                count += 1
                
        return count
            
                
            