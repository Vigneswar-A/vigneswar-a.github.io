class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        
        n = len(votes[0])
        scores = defaultdict(lambda : [0]*n)
        
        for rankings in votes:
            for i in range(n):
                scores[rankings[i]][i] -= 1

        return ''.join(sorted(votes[0], key=lambda c:(*scores.get(c), c)))
        