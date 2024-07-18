class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        adjacency = defaultdict(list)
        
        for u,v in roads:
            adjacency[u].append(v)
            adjacency[v].append(u)
            
            
        tree = defaultdict(list)
        
        stack = [0]
        visited = set()
        while stack:
            node = stack.pop()
            visited.add(node)
            for adj in adjacency[node]:
                if adj in visited:
                    continue
                tree[node].append(adj)
                stack.append(adj)
                
        sub_tree = {}
        def sub_tree_size(node):
            if not tree[node]:
                sub_tree[node] = 1
                return 1
            sub_tree[node] = sum(sub_tree_size(adj) for adj in tree[node])+1
            return sub_tree[node]
            
        sub_tree_size(0)
        
        cost_count = {0:0}
        def dfs(node=0):
            if not tree[node]:
                return 1
            cost = sum(dfs(adj) for adj in tree[node])
            cost_count[node] = cost
            return cost + sub_tree[node]//seats + (sub_tree[node]%seats != 0)
            
        dfs()
        return cost_count[0]