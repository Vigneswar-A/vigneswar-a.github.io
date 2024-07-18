class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
        counts = Counter({0 : 1})
        mask = 0
        res = 0
        for c in word:
            mask ^= (1 << (ord(c) - ord('a')))
            res += counts[mask]
            for letter in range(10):
                res += counts[mask^(1 << letter)]
            counts[mask] += 1
        return res
                
                
            

            