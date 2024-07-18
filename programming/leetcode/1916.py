class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        counts = Counter()
        
        for i,j in edges:
            counts[i] += 1
            counts[j] += 1
            
        return max(counts, key = counts.get)
            
        