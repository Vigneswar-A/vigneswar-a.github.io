
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        adjacency = [[] for _ in range(n)]
        
        hashmap = defaultdict(list)
        for i in range(n):
            hashmap[arr[i]].append(i)
            
        for i in range(n):
            if i:
                adjacency[i].append(i-1)
            if i+1 < n:
                adjacency[i].append(i+1)
            
        visited = set()
        queue = deque([0])
        dist = 0
        count = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == n-1:
                    return dist
                count += 1
                for adj in adjacency[node]+hashmap[arr[node]]:
                    if adj not in visited:
                        queue.append(adj)                 
                        visited.add(adj)
                hashmap[arr[node]].clear()
            dist += 1
            
        
        return 0    