class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        curr_neg = curr_pos = ans = 0
        for i in nums:
            if i > 0:
                curr_pos += 1
                curr_neg = (curr_neg+1) if curr_neg else 0
            elif i < 0:
                curr_neg, curr_pos = curr_pos+1, (curr_neg+1 if curr_neg else 0)
            else:
                curr_pos = curr_neg = 0
                
            ans = max(curr_pos , ans)
            
        return ans
        
        
                
                
        
        