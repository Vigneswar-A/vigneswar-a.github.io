class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def solve(src):
            
            dists = [inf]*n
            
            heap = [(src, 0)]
            heapq.heapify(heap)
            seen = set()
            while heap:
                node,cost = heapq.heappop(heap)
                if node in seen: continue
                seen.add(node)
                dists[node] = min(dists[node], cost)
                if edges[node] != -1:
                    heapq.heappush(heap, 
                            (edges[node], cost+1))
           
            return dists
            
            
            
        dists1 = solve(node1)
        dists2 = solve(node2)
        ans = min(range(n), key=lambda i:max(dists1[i],dists2[i]))
        
        return ans if dists1[ans] + dists2[ans] < inf else -1