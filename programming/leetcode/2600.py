class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        price.sort()
        
        def ispossible(res):
            prev = -inf
            count = 0
            for i in price:
                if i >= prev+res:
                    prev = i
                    count += 1
                    
                if count == k:
                    return 0
            return 1
        
        return bisect.bisect(range( max(price)-min(price)+1), 0, key=ispossible)-1
        
        
        
     

