# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return True
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
        edgeList.sort(key=lambda t:t[-1])
        self.adjacency = defaultdict(list)
        uf = UnionFind(n)
        for u,v,dist in edgeList:
            if uf.union(u, v): continue
            self.adjacency[u].append((v, dist))
            self.adjacency[v].append((u, dist))
            
    def query(self, p: int, q: int, limit: int) -> bool:
        queue = deque([p])
        visited = set()
        while queue:
            node = queue.popleft()
            if node == q:
                return True
            visited.add(node)
            for adj,cost in self.adjacency[node]:
                if cost < limit and adj not in visited:
                    queue.append(adj)
                
        return False
            
        


# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)