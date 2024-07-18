class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        count=0
        
        for i,n in enumerate(sorted(heights)):
            count+=n!=heights[i]
        
        return count
            
        