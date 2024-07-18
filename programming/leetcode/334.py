class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        i = j = k = float('inf')
        
        for n in nums:
            if n <= i:
                i = n
            elif n <= j:
                j = n
            elif n < k:
                return True
               
            
        return False
        
        