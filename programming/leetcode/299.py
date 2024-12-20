class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        counts = Counter(secret)
        bulls = 0
        cows = 0
        
        for s,g in zip(secret, guess):
            if s == g:
                bulls += 1
                if counts[s]:
                    counts[s] -= 1
                else:
                    cows -= 1
            elif counts[g]:
                cows += 1
                counts[g] -= 1
                
        return f"{bulls}A{cows}B"
                
                
        