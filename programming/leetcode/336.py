class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        indexmap = {word:i for i,word in enumerate(words)}
        res = []

        for word in words:
            if word[::-1] in indexmap:
                idx1, idx2 = indexmap[word], indexmap[word[::-1]]
                if idx1 != idx2:                                            
                    res.append((idx1, idx2))
                        
            for i in range(1, len(word)):
                suffix = word[:i-1:-1]
                prefix = word[i-1::-1]
                if word[:i] == prefix and suffix in indexmap:
                    idx1, idx2 = indexmap[suffix], indexmap[word]
                    if idx1 != idx2:                                            
                        res.append((idx1, idx2))
                        
                if word[i:] == suffix and prefix in indexmap:
                    idx1, idx2 = indexmap[word], indexmap[prefix]
                    if idx1 != idx2:                                            
                        res.append((idx1, idx2))

        if "" in indexmap:
            idx = indexmap[""]
            for i in range(len(words)):
                if i == idx:
                    continue
                if words[i] == words[i][::-1]:
                    res.append((idx, i))
                    res.append((i, idx))
        return res
                
                
            
        