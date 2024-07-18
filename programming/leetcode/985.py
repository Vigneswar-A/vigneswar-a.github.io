class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        queue = deque(tokens)
        
        score = 0
        max_score = 0
        while queue:
            if power >= queue[0]:
                score += 1
                power -= queue.popleft()              
                max_score = max(max_score, score)
            
            elif score:
                score -= 1
                power += queue.pop()
                
            else:
                break
                
        return max_score

                
            
            
                
            
        