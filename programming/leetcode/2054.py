from sortedcontainers import SortedList
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        max_time = max(sum(times, []))
        times = [*sorted([(i,u,v) for i,(u,v) in enumerate(times)], key=lambda a:(a[1],a[2]))]
        t = 0
        leaving = defaultdict(list)
        free = [*range(len(times))]
        heapify(free)
        for i in range(max_time):
            for seat in leaving[i]:
                heappush(free, seat)
                
            if i >= times[t][1]:
                seat = heappop(free)
                if times[t][0] == targetFriend:
                    return seat
                leaving[times[t][2]].append(seat)
                t += 1
            
            
        
                
                
                
                
        
        
            
        