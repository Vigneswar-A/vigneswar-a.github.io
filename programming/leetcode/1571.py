class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        
        @cache
        def calculate_distance(i, j):
            median = houses[i+j >> 1]
            return sum(abs(houses[x]-median) for x in range(i,j+1))
        
        n = len(houses)

        @cache
        def dp(start=0, k=k):
            if k == 1:
                return calculate_distance(start, n-1)
            
            res = float('inf')
            for nxt in range(start+1, n):
                res = min(res, dp(nxt, k-1)+calculate_distance(start, nxt-1))

            return res

        
        return dp()
                