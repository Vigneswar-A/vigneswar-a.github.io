class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:      
        prefix = [0 , *accumulate(cardPoints)]
        window = len(prefix) - k - 1
        return prefix[-1] - min(prefix[i + window] - prefix[i] for i in range(k + 1))
                
        
                
                
                