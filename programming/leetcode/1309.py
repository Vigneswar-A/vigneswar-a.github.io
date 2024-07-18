class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        
        # create nodes , here groups are individual nodes
        nodes = [[] for _ in range(m)]
        hashmap = [-1]*n
        
        for i in range(m):
            nodes[i] = []
        
        for i in range(n):
            if group[i] != -1:
                nodes[group[i]].append(i)
                hashmap[i] = group[i]
            else:
                nodes.append([i])
                hashmap[i] = len(nodes)-1
            
    
        n = len(nodes)
        adjacency = [[] for _ in range(n)]
        indegree = [0]*n
        
        group_adjacency = [defaultdict(list) for _ in range(n)]
        group_indegree = [Counter() for _ in range(n)]
        
        # topological sort for groups
        for i,items in enumerate(beforeItems):
            for j in items:
                u = hashmap[i]
                v = hashmap[j]
                if u == v:
                    group_adjacency[u][j].append(i)
                    group_indegree[u][i] += 1
                    continue
                adjacency[v].append(u)
                indegree[u] += 1
        
        for i in range(n):
            group = nodes[i]
            adjs = group_adjacency[i]
            indeg = group_indegree[i]
            temp = []
            queue = deque([node for node in group if indeg[node] == 0])

            while queue:
                node = queue.popleft()
                temp.append(node)
                for adj in adjs[node]:
                    indeg[adj] -= 1
                    if indeg[adj] == 0:
                        queue.append(adj)
            nodes[i] = temp
            if any(indeg.values()):
                return []
                
            
        queue = deque([node for node in range(n) if indegree[node] == 0])
        res = []
        
        while queue:
            node = queue.popleft()
            res.extend(nodes[node])
            for adj in adjacency[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
                    
        if any(indegree):
            return  []
        return res
        
                    
        
        
                
                
            
            
        

        
        