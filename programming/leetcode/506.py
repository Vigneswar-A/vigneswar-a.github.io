class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        rankgen = enumerate(sorted(score, reverse=1), 1)
        ranks = {}
        
        try:
            ranks[next(rankgen)[1]] = "Gold Medal"
            ranks[next(rankgen)[1]] = "Silver Medal"
            ranks[next(rankgen)[1]] = "Bronze Medal"  
        except: #StopIteration
            pass

        for rank, scr in rankgen:
            ranks[scr] = str(rank)
        
        
        return [*map(ranks.get, score)]