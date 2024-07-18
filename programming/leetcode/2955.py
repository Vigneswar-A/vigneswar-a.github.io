class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        return 100-min(ceil(purchaseAmount/10)*10, floor(purchaseAmount/10)*10, key=lambda i : abs(i-purchaseAmount))