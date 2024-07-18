class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        hashmap = defaultdict(list , {word : [word] for word in sentence1 + sentence2})
        
        for u,v in similarPairs:
            hashmap[u].append(v)
            hashmap[v].append(u)
            
        for u,v in zip(sentence1 , sentence2):
            if not (v in hashmap[u] or u in hashmap[v]):
                return False
            
        return True
                
        