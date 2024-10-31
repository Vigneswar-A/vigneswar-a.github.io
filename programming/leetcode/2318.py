class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        result = None
        temp = [0]*12
        max_score = 0
        def backtrack(i, remaining, score):
            if i == 12:
                nonlocal max_score
                nonlocal result
                if score > max_score:
                    temp[-1] += remaining
                    result = temp[:]
                    max_score = score
                return
            
            if remaining > aliceArrows[i]:
                temp[i] = aliceArrows[i]+1
                backtrack(i+1, remaining-aliceArrows[i]-1, score+i)
                temp[i] = 0
            backtrack(i+1, remaining, score)
            
        backtrack(0, numArrows, 0)
        return result
            
        