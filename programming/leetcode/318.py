class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        bits = set()
        for word in words:
            mask = 0
            for c in word:
                mask |= (1 << ord(c) - ord('a'))
            bits.add((len(word), mask))
        bits = list(bits)
            
        ans = 0
        for i in range(len(bits)):
            for j in range(i+1, len(bits)):
                len1, mask1 = bits[i]
                len2, mask2 = bits[j]
                if mask1&mask2 == 0:
                    ans = max(ans, len1*len2)
                    
        return ans
                    
        