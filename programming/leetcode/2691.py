class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        prefix = []
        count = 0
        
        for word in words:
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                count += 1
            prefix.append(count)
        prefix.append(0)
            
        res = []
        for l,r in queries:
            res.append(prefix[r]-prefix[l-1])
            
        return res
            