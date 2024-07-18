class Solution:
    def getLucky(self, s: str, k: int) -> int:
        transform = ''.join(str(ord(c) - 96) for c in s)
        for _ in range(k):
            transform = str(sum(map(int , transform)))
            
        return int(transform)
            
        