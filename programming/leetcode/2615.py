class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1 = [0]*26
        count2 = [0]*26
        
        for c in word1:
            count1[ord(c)-ord('a')] += 1
        
        for c in word2:
            count2[ord(c)-ord('a')] += 1
            
        for i in range(26):
            for j in range(26):
                if count1[i] == 0 or count2[j] == 0:
                    continue
                count1[j] += 1
                count1[i] -= 1
                count2[j] -= 1
                count2[i] += 1
                if sum(k >= 1 for k in count1) == sum(k >= 1 for k in count2):
                    return True
                count1[j] -= 1
                count1[i] += 1
                count2[j] += 1
                count2[i] -= 1
    
                
            
                
    
    
        
                
                
            
                