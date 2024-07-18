class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        def is_valid(h):
            atleast = 0
            for citation in citations:
                if citation >= h:
                    atleast += 1
            return atleast < h
        return bisect.bisect_right(range(1, n+1), 0, key = is_valid)
                    