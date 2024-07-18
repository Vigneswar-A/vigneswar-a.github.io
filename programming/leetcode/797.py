class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        counts = Counter(answers)
        res = 0
        for i, c in counts.items():
            res += ceil(c/(i+1))*(i+1)
            
        return res
            
        