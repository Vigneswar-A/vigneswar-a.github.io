class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        current = nums[0]
        
        for i in nums:
            if current != i:
                if k > i - current:
                    k -=  i - current
                    current += i - current
                else:
                    break
                
            if not k:
                return current
            
            current += 1
            
        return current + k - 1
            
        
                
            
            
            
        
                
        