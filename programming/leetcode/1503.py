class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        @cache
        def dp(i=0, j=1):
            if i == len(satisfaction):
                return 0
            return max(satisfaction[i]*j+dp(i+1, j+1), dp(i+1, j))
        
        return dp()
                       
                       
            
            
        