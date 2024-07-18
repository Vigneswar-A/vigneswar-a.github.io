class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dp(i=0, op=0, s=''):
            if i == 2*n: return [s] if not op else []
            return (dp(i+1, op-1, s+')') if op else []) + dp(i+1, op+1, s+'(') 
                
        return dp()
            
            