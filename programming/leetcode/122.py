class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        prev = inf
        res = 0
        
        for i in prices:
            if prev < i:
                res += i-prev
            prev = i
        
        return res

            
        