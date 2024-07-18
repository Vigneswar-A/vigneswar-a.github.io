class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=1)
        return sum(cost)-sum(cost[2::3])