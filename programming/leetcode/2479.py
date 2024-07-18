class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        counts = [0]*n
        free = [*range(n)]
        heapify(free)
        occupied = []
        print(meetings)
        for start, end in meetings:
            while occupied and heapq.nsmallest(1, occupied )[0][0] <= start:
                time, room = heappop(occupied)
                heappush(free, room)
            if not free:
                time, room = heappop(occupied)
                counts[room] += 1
                heappush(occupied, (time+(end-start), room))
            else:
                room = heappop(free)
                counts[room] += 1
                heappush(occupied, (end, room))
                
        
        return max(range(n), key=lambda i : counts[i])
           
                
                
                
                
        
        
        