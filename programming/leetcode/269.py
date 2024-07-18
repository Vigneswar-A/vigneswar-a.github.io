class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        letters = set(''.join(words))
        
        edges = set()
        prefix = {"":words}
        
        # create edges
        for _ in range(max(map(len, words))):
            new_prefix = defaultdict(list)
            
            # invalid input detection ["abc", "ab"]
            for pre, words in prefix.items():
                if any(words[i] == '' and words[i-1] != '' for i in range(1, len(words))):
                    return ""
                
            for pre,words in prefix.items():
                for i in range(len(words)):
                    if not words[i]:
                        continue
                    new_prefix[pre+words[i][0]].append(words[i][1:])
                    if i and words[i-1] and words[i-1][0] != words[i][0]:
                        edges.add((words[i][0], words[i-1][0]))
                prefix = new_prefix
                     
        # create graph for topological sorting
        in_degree = Counter()
        adjacency = defaultdict(list)

        for u,v in edges:
            in_degree[u] += 1
            adjacency[v].append(u)

        # cycle test ["z", "x", "z"]
        if edges: 
            visited = set()
            for startnode in list(adjacency):
                visited.clear()
                queue = deque([startnode])
                while queue:
                    node = queue.popleft()
                    visited.add(node)
                    for adj in adjacency[node]: 
                        if adj == startnode:
                            return ''
                        if adj in visited:
                            continue
                        queue.append(adj)
         
        # topological sort
        queue = deque([node for node in letters if in_degree[node] == 0])
        res = ''

        while queue:
            node = queue.popleft()
            res += node
            for adj in adjacency[node]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
                    
        return res
            