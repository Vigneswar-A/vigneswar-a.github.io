class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = len(digits) - 1
        rem = 1
        while r + 1:
            rem , digits[r] = divmod(digits[r] + rem , 10)
            r -= 1
        
        if rem:
            digits = [rem] + digits
            
        return digits
        