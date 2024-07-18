class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        seen = set()
        
        def find_paths(node , path):
            path.append(node)
            if node == target:
                res.append(path)
            [find_paths(node , path[:]) for node in graph[node]]
            
            
            
        find_paths(0 , [])
        
        return res
        
            
        
            
        