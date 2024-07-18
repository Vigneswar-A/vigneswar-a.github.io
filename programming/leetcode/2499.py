class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        transactions.sort(key=lambda arr:((0, arr[1]) if arr[0] >= arr[1] else (1, -arr[0])))
        money = 0
        res = 0
        for cost, cashback in transactions:
            res += max(cost-money, 0)
            money = max(money-cost, 0)+cashback
            
        return res
            
        