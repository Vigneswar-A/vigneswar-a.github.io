class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = Counter((t%60 for t in time))
        
        res = 0
        seen = set()
        for t in counts:
            if -t%60 == t:
                res += comb(counts[t], 2)
            elif -t%60 in counts and (t, -t%60) not in seen:
                res += counts[t] * counts[-t%60]
                seen.add((-t%60, t))

        return res
                
        
        
                    
        