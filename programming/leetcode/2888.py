class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        dom = max(counts, key=counts.get)
        total = counts[dom]
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == dom:
                count += 1
            
            if 2*count > i+1 and (total-count)*2 > n-i-1:
                return i
            
        return -1
                
        
        
        
        
        