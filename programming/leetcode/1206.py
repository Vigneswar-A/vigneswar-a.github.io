class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        res = [0]*(n+1)
        
        for i,j,c in bookings:
            res[i-1] += c
            res[j] -= c
        res.pop()
        return list(accumulate(res))
            
        