class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        res = defaultdict(list)
        
        def abbr(word, i):
            return min(word, word[:i+1]+str(len(word)-i-2)+word[-1], key=len)
        
        for word in words:
            res[abbr(word, 0)].append(word)
        
        while True:
            for key,vals in res.copy().items():
                if len(vals) > 1:
                    del res[key]
                    i = sum(1 for _ in takewhile(str.isalpha, key))
                    for val in vals:        
                        res[abbr(val, i)].append(val)
                    break
            else:
                break

        res = {v[0]:k for k,v in res.items()}
        return [res[word] for word in words]

                
                    
            