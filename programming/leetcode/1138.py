class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        extras = [0]
        total = 0
        for i in range(n):
            extras.append(extras[-1]+customers[i]*grumpy[i])
            total += customers[i]*(1-grumpy[i])
        res = 0
        for i in range(len(extras)-minutes):
            res = max(res, (extras[i+minutes]-extras[i]))
        return res+total
            