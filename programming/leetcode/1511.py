class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        @cache
        def dp(i=0 , greater=True, count=0):
            if count == 2:
                return 1
            res = 0
            for j in range(i+1,len(rating)):
                if greater and rating[j] > rating[i]:
                    res += dp(j,True,count+1)
                
                if not greater and rating[j] < rating[i]:
                    res += dp(j,False,count+1)
            return res
        
        res = 0
        for i in range(len(rating) - 2):
            res += dp(i , True) + dp(i , False)
            
        return res