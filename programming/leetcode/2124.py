class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        
        visits = defaultdict(list)
        
        for i,room in enumerate(nextVisit):
            visits[room].append(i)
            
        n = len(nextVisit)
        odd = [inf]*n
        even = [inf]*n
        odd[0] = 0
        even[0] = 1
        
        for i in range(1, n):
            odd[i] = (even[i-1]+1)%(10**9+7)
            even[i] = (2*odd[i]-odd[nextVisit[i]]+1)%(10**9+7)
            
        return odd[-1]%(10**9+7)