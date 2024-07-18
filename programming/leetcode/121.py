class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minsofar = inf
        res = 0
        
        for i in prices:
            minsofar = min(minsofar, i)
            res = max(res, i-minsofar)
            
        return res
        