class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        
        counts = Counter()
        
        
        
        for i in range(0, len(word), k):
            counts[word[i:i+k]] += 1
        
        return len(word)//k-max(counts.values())
            
       
            

        
        