class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        i , size = 0 , len(sequence)
        j , n = 0 , len(word)
        
        dest = 0 
        max_k = k = 0
        
        while i < size:
            
            if sequence[i] == word[j]:
                j += 1
                dest = j
                
            else:
                i -= (k * n or j)
                j = k = 0
                         
            if j == n:
                k += 1
                j = 0
                        
            i += 1    
            max_k = max(k , max_k)
            
        return max_k          