class Leaderboard:

    def __init__(self):
        self.scores = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        return sum(islice(sorted(self.scores.values(), reverse=1), K))
        

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)