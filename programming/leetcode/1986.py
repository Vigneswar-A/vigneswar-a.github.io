class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        if not edges: 
            return 1
        n = len(set(colors))
        m = max(map(max, edges))+1
        
        dp = defaultdict(lambda : [0]*m)
        
        queue = deque([])
        degree = [0]*m
        adjacency = [[] for _ in range(m)]
        
        for u,v in edges:
            degree[v] += 1
            adjacency[u].append(v)
            
        queue = deque([node for node in range(m) if degree[node] == 0])
        color_set = set(colors)
        if not queue:
            return -1
        
        visited = 0
        while queue:
            node = queue.popleft()
            dp[colors[node]][node] += 1
            visited += 1
            for adj in adjacency[node]:
                for color in color_set:
                    dp[color][adj] =  max(dp[color][node], dp[color][adj])
                degree[adj] -= 1
                if degree[adj] == 0:
                    queue.append(adj)

        if visited < len(colors):
            return -1
        
        return max(map(max, dp.values()))
            
        
        