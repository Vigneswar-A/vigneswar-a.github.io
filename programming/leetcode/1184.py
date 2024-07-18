class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda arr:arr[1])
        stoppings = []
        people = 0
        
        for n,u,v in trips:
            people += n
            heapq.heappush(stoppings, (v,n))
            
            while heapq.nsmallest(1, stoppings)[0][0] <= u:
                _,down = heapq.heappop(stoppings)
                people -= down

            if people > capacity:
                return False
            
        return True
                
            
            
            