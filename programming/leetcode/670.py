class Solution:
    def maximumSwap(self, num: int) -> int:
        
        digits = list(map(int, str(num)))
        counts = Counter(digits)
        j = -1
        for i in range(len(digits)):
            if j != -1:
                i -= 1
                break
            for greater in range(9, digits[i], -1):
                if counts[greater]:
                    j = len(digits) - digits[::-1].index(greater) - 1
                    break
            counts[digits[i]] -= 1
            
        digits[i], digits[j] = digits[j], digits[i]
        
        return "".join(map(str, digits))