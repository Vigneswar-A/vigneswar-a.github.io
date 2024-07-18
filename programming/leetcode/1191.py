class UnionFind:
    def __init__(self , size):
        self.root = [*range(size)]
        self.rank = [1] * size
        
    def find(self , x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self , x , y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        
        if self.rank[x] > self.rank[y]:
            self.root[y] = x
        elif self.rank[y] > self.rank[x]:
            self.root[x] = y
        else:
            self.rank[x] += 1
            self.root[y] = x
            
    def is_connected(self , x , y):
        return self.find(x) == self.find(y)
            
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        hashmap = {}
        revmap = {}
        words_with_synonyms = set(itertools.chain.from_iterable(synonyms))
        for i , word in enumerate(words_with_synonyms):
            hashmap[word] = i
            revmap[i] = word
            
        size = len(hashmap)
        connect = UnionFind(size)
        
        for u , v in synonyms:
            connect.union(hashmap[u] , hashmap[v])

        
        sentence = tuple(text.split())
        res = set([sentence])
        for i in range(len(sentence)):
            if sentence[i] in words_with_synonyms:
                temp = list(res)
                for newword in temp:
                    for another_word in words_with_synonyms:
                        if connect.is_connected(hashmap[newword[i]] , hashmap[another_word]):
                            res.add(newword[:i] + (another_word,) + newword[i + 1:])
            
                            
        return sorted(map(' '.join , res))
                                  
                                  
            
            
        
            
        
        
            
        
            
        
        
        