class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        for n in range(1 , 2 * ceil(len(b)/len(a)) + 1):
            if b in a * n:
                return n
            
        return -1
            
        