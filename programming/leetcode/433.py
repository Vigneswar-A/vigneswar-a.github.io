class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        def one_dist(str1, str2):
            return sum(c1 != c2 for c1,c2 in zip(str1, str2)) == 1
        
        dist = -1
        queue = deque([startGene])
        visited = set()
        while queue:
            dist += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node == endGene:
                    return dist
                for gene in bank:
                    if one_dist(gene, node):
                        queue.append(gene)

        return -1
                
        