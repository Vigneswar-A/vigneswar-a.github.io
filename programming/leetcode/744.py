class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjacency = [[] for _ in range(n)]
        
        for u, v, t in times:
            adjacency[u - 1].append((v - 1 , t))
        
        dist_from_src = [float('inf') for _ in range(n)]    
        dist_from_src[k - 1] = 0
        
        heap = [(0 , k - 1)]
        heapq.heapify(heap)
        
        seen = set()
        
        while heap:
            currtime , currnode = heapq.heappop(heap)
            seen.add(currnode)
            
            for node , time in adjacency[currnode]:       
                if node not in seen and currtime + time < dist_from_src[node]:
                    dist_from_src[node] = currtime + time
                    heapq.heappush(heap , (currtime + time , node))

        res = max(dist_from_src)
        
        return res if res != float('inf') else -1