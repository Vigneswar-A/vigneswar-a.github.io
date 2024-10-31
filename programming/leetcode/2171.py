class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        adjacency = defaultdict(list)
        
        for u,v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
            
        heap = [(0, 1)]
        reached = None
        
        dist_from_src = [inf]*(n+1)
        dist2_from_src = [inf]*(n+1)
        dist_from_src[0] = 0
        dist2_from_src[0] = 0
        
        while heap:
            curr_time, curr_node = heappop(heap)
            if curr_node == n and reached is not None and reached != curr_time:
                return curr_time
            elif curr_node == n:
                reached = curr_time

            if (curr_time//change)%2 == 0:
                travel_time = curr_time+time
            else:
                travel_time = (curr_time//change+1)*change+time

            for adj in adjacency[curr_node]:
                if dist_from_src[adj] == inf:
                    dist_from_src[adj] = curr_time
                    heappush(heap, (travel_time, adj))
                elif dist2_from_src[adj] == inf and dist_from_src[adj] != curr_time:
                    dist2_from_src[adj] = curr_time
                    heappush(heap, (travel_time, adj))
                
                    
        
        