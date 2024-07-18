class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix = []
        count = 0
        for c in customers:
            if c == 'Y':
                count += 1
            prefix.append(count)
            
        min_val = inf
        min_idx = 0
        
        for i in range(n+1):
            penalty = (prefix[-1]-(prefix[i-1] if i else 0)) + (i-(prefix[i-1] if i else 0))
            if penalty < min_val:
                min_idx = i
                min_val = penalty
                
        return min_idx
            
                
        
        
        