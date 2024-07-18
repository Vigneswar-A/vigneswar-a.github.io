class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        
        counts = Counter(candies)
        res = 0
        n = len(candies)
        
        for i in range(min(n, k)):
            counts[candies[i]] -= 1
            if counts[candies[i]] == 0:
                del counts[candies[i]]
                
        res = len(counts)
        for i in range(k, n):
            counts[candies[i-k]] += 1
            counts[candies[i]] -= 1
            if counts[candies[i]] == 0:
                del counts[candies[i]]
            res = max(res, len(counts))
            
        return res
        
            
            