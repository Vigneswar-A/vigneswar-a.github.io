class Solution:
    def reformatNumber(self, number: str) -> str:
        
        
        digits = number.replace(" ", "").replace("-", "")
        
        pairs = [digits[i:i+3] for i in range(0, len(digits), 3)]
        
        if len(pairs[-1]) == 1:
            pairs[-2:] = [pairs[-2][:2], pairs[-2][-1] + pairs[-1][-1]]
            

        return "-".join(pairs)