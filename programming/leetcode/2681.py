class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        split_points = []
        for i in range(len(weights)-1):
            split_points.append((weights[i]+weights[i+1]))
        split_points.sort()

        return sum(split_points[-k+1:]) - sum(split_points[:k-1])
                   
                   
            
            
            
        
                