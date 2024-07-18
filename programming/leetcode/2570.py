class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        
        
        @cache
        def dp(idx=0, amount=maxAmount, coupons=maxCoupons):
            if amount < 0 or coupons < 0:
                return -inf
            
            if idx == len(price):
                return 0
            
            return max(
                dp(idx+1, amount-price[idx], coupons) + tastiness[idx],
                dp(idx+1, amount-price[idx]//2, coupons-1) + tastiness[idx],
                dp(idx+1, amount, coupons)
            )
        
        
        return dp()
            
        