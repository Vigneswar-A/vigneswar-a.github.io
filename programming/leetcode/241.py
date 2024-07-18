class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        
        exp = re.findall(r'\d+|.', expression)
        op = {"+" : int.__add__, "-" : int.__sub__, "*" : int.__mul__}
        
        @cache
        def dp(left=0, right=len(exp)-1):
            if left == right:
                return [int(exp[left])]
            res = []
            for i in range(left, right+1):
                if not exp[i].isnumeric():
                    res.extend(op[exp[i]](l, r) for l in dp(left, i-1) for r in dp(i+1, right))
            return res
                    
        return dp()
            
            
            
        
        