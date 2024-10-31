class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        counts = Counter()
        res = []
        colors = Counter()
        for x,y in queries:
            if colors[x]:
                counts[colors[x]] -= 1
                if counts[colors[x]] == 0:
                    del counts[colors[x]]
            counts[y] += 1
            colors[x] = y
            res.append(len(counts))
            
        return res
               
        