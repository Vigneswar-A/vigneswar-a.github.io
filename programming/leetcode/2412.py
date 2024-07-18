class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        
        a, b, c = amount
        seconds = 0
        
        while a or b or c:
            a, b, c = sorted([a, b, c])
            if b and c:
                b -= 1
            c -= 1
            seconds += 1
                
        return seconds
        
                
        
        
            
                