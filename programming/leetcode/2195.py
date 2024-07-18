class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(t, tickets[k]) for t in tickets[:k + 1]) + sum(min(t, tickets[k] - 1) for t in tickets[k + 1:])