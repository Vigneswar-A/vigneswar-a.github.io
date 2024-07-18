class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort(key=lambda a:(a[0], -a[1]))
        
        prices = []
        
        maxb = -inf
        for p,b in items:
            if prices and p == prices[-1][0]:
                continue
            maxb = max(maxb, b)
            prices.append((p, maxb))
        res = []
        
        for p in queries:
            j = bisect.bisect(prices, (p,inf))-1
            
            if j == -1:
                res.append(0)
            else:
                res.append(prices[min(j, len(prices)-1)][-1])
                
        return res
            
            
            
            
            
            
                   
                   
        