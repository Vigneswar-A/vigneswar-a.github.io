class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        odds = 0
        for count in Counter(s).values():
            if count%2:
                odds += 1
                
        return odds <= k
            
        