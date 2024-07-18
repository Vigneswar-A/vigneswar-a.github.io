class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adjacency = [[] for _ in range(n)]
        seen = set([0])

        for u,v in edges:
            if u in seen:
                adjacency[u].append(v)
                seen.add(v)
            elif v in seen:
                adjacency[v].append(u)
                seen.add(u)

        @cache
        def apple_in_subtree(root):
            if hasApple[root]:
                return True

            return any(apple_in_subtree(adj) for adj in adjacency[root])
        

        def dfs(root=0):
            if not adjacency[root]:
                return 0
                
            res = 0
            for adj in adjacency[root]:
                if apple_in_subtree(adj):
                    res += 2 + dfs(adj)
            
            return res

        return dfs()





        