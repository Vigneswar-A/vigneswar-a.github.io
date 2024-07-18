class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda arr : arr[0] - arr[1])
        n = len(costs)//2
        return sum(costs[i][0]+costs[n+i][1] for i in range(n))