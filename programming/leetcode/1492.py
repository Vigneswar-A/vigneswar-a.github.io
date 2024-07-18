class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        
        received = [inf]*n
        received[headID] = 0
        
        adjacency = defaultdict(list)
        
        for i,manager in enumerate(manager):
            adjacency[manager].append(i)
            
        stack = [headID]
        while stack:
            node = stack.pop()
            for adj in adjacency[node]:
                received[adj] = min(received[node]+informTime[node], received[adj])
                stack.append(adj)
                
        return max(received)
            