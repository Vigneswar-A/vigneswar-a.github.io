class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        is_heavy = mass >= 100
        
        is_bulky = any(d >= 10**4 for d in [length, width, height]) or length*width*height >= 10**9
        
        if is_heavy and is_bulky:
            return "Both"
        elif is_heavy:
            return "Heavy"
        elif is_bulky:
            return "Bulky"
        else:
            return "Neither"
        
        