class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c = Counter(s)
        t = Counter(target)
        count = 0
        while c >= t:      
            c -= t
            count += 1
            
        return count
        