class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        m = max(nums)+1
        c = Counter(nums)
        counts = [0]*m
        
        for i,c in c.items():
            for j in range(i, m, i): 
                counts[j] += c
                
        counts = list(accumulate(counts))
        
        return sum(counts[i] for i in nums)%1000000007
            
            
            
        
        