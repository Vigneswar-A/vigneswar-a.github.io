class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        count = [0]*26
        
        
        for c in word:
            count[ord(c)-ord('a')] += 1
            
        for i in range(26):
            count[i] -= 1
            if len(set(count).difference({0})) == 1:
                return True
            count[i] += 1
            
        return False
        