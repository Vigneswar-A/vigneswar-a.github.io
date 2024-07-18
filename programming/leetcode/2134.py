class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        res = 0
        counts = Counter()
        counts['T'] = counts['F'] = 0
        for right in range(len(answerKey)):
            counts[answerKey[right]] += 1
            if min(counts.values()) <= k:
                res += 1
            else:
                counts[answerKey[right-res]] -= 1     
        return res
            
                
        