class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        
        adj = defaultdict(list)
        
        for node in range(nodes):
            adj[parent[node]].append(node)
            
        @cache
        def get_sub_sum(node):
            total = value[node]
            for child in adj[node]:
                total += get_sub_sum(child)
            return total
        
        deleted_roots = set()
        for node in range(nodes):
            if get_sub_sum(node) == 0:
                deleted_roots.add(node)
                
        deleted_nodes = set()
        for root in deleted_roots:
            stack = [root]
            while stack:
                node = stack.pop()
                deleted_nodes.add(node)
                stack.extend(adj[node])
                
        return nodes - len(deleted_nodes)
                
        
                
                
                
                
                
            