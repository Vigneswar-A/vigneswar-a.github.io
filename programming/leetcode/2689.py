class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        
        n = len(basket1)
        
        freq1 = Counter()
        freq2 = Counter()
        minval = inf

        for i in range(n):
            freq1[basket1[i]] += 1
            freq2[basket2[i]] += 1
            minval = min(minval, basket1[i], basket2[i])
            
        resultant = (freq1+freq2)
        if any(v%2 for v in resultant.values()):
            return -1
        
        swap1 = []
        swap2 = []
        for i in resultant:
            if freq1[i] != resultant[i]//2:
                swap1.extend([i]*(resultant[i]//2-freq1[i]))
            if freq2[i] != resultant[i]//2:
                swap2.extend([i]*(resultant[i]//2-freq2[i]))
                
        swap1.sort()
        swap2.sort(reverse=1)
        
        res = 0
        for i in range(len(swap1)):
            res += min(swap1[i], swap2[i], 2*minval)
            
        return res
                
            
        
        
        
        
            
        
    
    
        