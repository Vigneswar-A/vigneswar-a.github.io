class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = inf
        
        for i in prices:
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
                
        return money-min1-min2 if min1+min2 <= money else money
            