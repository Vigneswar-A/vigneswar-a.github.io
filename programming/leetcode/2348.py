class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        letters = [0, 0, 3, 3, 3, 3, 3, 4, 3, 4]
        res = 1
        
        @cache
        def dp3(i):
            prev_1, prev_2, curr = 0, 0, 1
            
            for _ in range(i):
                prev_1, prev_2, curr = prev_2, curr, curr+prev_1+prev_2
                
            return curr
        
        @cache
        def dp4(i):
            prev_1, prev_2, prev_3, curr = 0, 0, 0, 1
            
            for _ in range(i):
                prev_1, prev_2, prev_3, curr = prev_2, prev_3, curr, prev_1 + prev_2 + prev_3 + curr
                
            return curr
                
        for k,v in groupby(pressedKeys):
            if k == '7' or k == '9': 
                res *= dp4(sum(1 for _ in v))
            else:
                res *= dp3(sum(1 for _ in v))
            
        return res%(1000000007)
            
        