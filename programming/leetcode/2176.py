class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        degree = [0]*n
        adj = defaultdict(list)
        
        for u,v in relations:
            degree[v-1] += 1
            adj[u-1].append(v-1)
            
        heap = []
        for i in range(n):
            if degree[i] == 0:
                heappush(heap, (time[i], i))

        currtime = 0
        while heap:
            currtime,node = heappop(heap)
            for adjnode in adj[node]:
                degree[adjnode] -= 1
                if degree[adjnode] == 0:
                    heappush(heap, (currtime+time[adjnode], adjnode))
                    
        return currtime
            
        