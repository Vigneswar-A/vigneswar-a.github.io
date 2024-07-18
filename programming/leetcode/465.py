class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        cash = Counter()
        
        for u,v,c in transactions:
            cash[u] -= c
            cash[v] += c
            
        positive = []
        negative = []
        
        for person,amount in cash.items():
            if amount > 0:
                positive.append(amount)
            elif amount < 0:
                negative.append(-amount)
                

        
        def backtrack(idx=0):
            
            if not any(positive) and not any(negative):
                return 0
            res = inf
            for i in range(len(positive)):
                amount = positive[i]
                if amount == 0:
                    continue
                if negative[idx] > amount:
                    positive[i] = 0
                    negative[idx] -= amount
                    res = min(res, backtrack(idx)+1)
                    negative[idx] += amount
                    positive[i] = amount
                else:
                    temp = negative[idx]
                    positive[i] -= negative[idx]
                    negative[idx] = 0
                    res = min(res, backtrack(idx+1)+1)
                    negative[idx] = temp
                    positive[i] += negative[idx]
            return res
        
        return backtrack()
                
                
                