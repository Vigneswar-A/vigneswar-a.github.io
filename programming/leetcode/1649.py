class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        
        total = 0
        hashset = {0}
        count = 0
        
        for i in nums:
            total += i
            if total - target in hashset:
                count += 1
                hashset.clear()
                hashset.add(0)
                total = 0
            hashset.add(total)
            
        return count
        
            
        
                
        
        