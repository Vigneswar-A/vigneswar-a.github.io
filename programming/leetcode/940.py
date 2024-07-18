class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        counts = Counter()
        
        l = r = 0
        
        res = 0
        
        while r < len(fruits):
            counts[fruits[r]] += 1
            r += 1
            
            while len(counts) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
                l += 1
                
            res = max(res, r-l)
            
        return res
                
            
                
            
        