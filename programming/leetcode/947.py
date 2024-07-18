class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winners = []
        counts = Counter()
        recent = {}
        
        for i, (time, person) in enumerate(sorted(zip(times, persons))):
            counts[person] += 1
            recent[person] = i
            self.winners.append((time, max(counts, key=lambda p: (counts.get(p),recent[p]))))

    def q(self, t: int) -> int:
        return self.winners[bisect.bisect_right(self.winners, t, key = lambda tup:tup[0])-1][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)