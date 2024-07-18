class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        
        def is_citation(n):
            count = 0
            for citation in citations:
                if citation >= n:
                    count += 1
            return count < n

        return bisect.bisect_left(range(len(citations)+1), 1, key=is_citation) - 1
        