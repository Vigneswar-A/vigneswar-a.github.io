class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        max_val = -inf
        
        for i in map(int, re.findall(r"\d+", s)):
            if i <= max_val:
                return False
            max_val = i
            
        return True
        