class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        scores = defaultdict(lambda:0)
        for i,node in enumerate(edges):
            scores[node] += i
        
        return max(scores , key=(lambda node : (scores[node] , -node)))
            
        
                    