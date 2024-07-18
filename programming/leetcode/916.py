class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for c in s:
            if c.isdigit():
                length *= int(c)
            else:
                length += 1
    
        for c in s[::-1]:
            k %= length
            
            if c.isdigit():
                length //= int(c)
            else:
                if k == 0: return c
                length -= 1
            