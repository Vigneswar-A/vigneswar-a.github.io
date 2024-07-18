class UnionFind:
    def __init__(self , size):
        self.root = [*range(size)]
        self.rank = [1] * size
        
    def find(self , x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self , x , y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        
        if self.rank[x] > self.rank[y]:
            self.root[y] = self.root[x]
        elif self.rank[y] > self.rank[x]:
            self.root[x] = self.root[y]
        else:
            self.rank[x] += 1
            self.root[y] = x
            
        return True
    
    def is_connected(self , x , y):
        return self.find(x) == self.find(y)
    
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        n = itertools.count()
       
        hashmap = defaultdict(partial(next , n))
        connect = UnionFind((len(similarPairs) + 1) * 2)
        
        for u,v in similarPairs:
            connect.union(hashmap[u] , hashmap[v])
                

        
        return all(connect.is_connected(hashmap[u] , hashmap[v]) for u,v in zip(sentence1 , sentence2))
            
        