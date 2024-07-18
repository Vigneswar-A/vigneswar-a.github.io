class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 1000000007
        people = [[] for _ in range(41)]
        
        for i in range(len(hats)):
            for hat in hats[i]:
                people[hat].append(i)
                
        people = list(filter(None, people))

        @cache
        def dp(mask=0, idx=len(people)-1):
            if mask.bit_count() == len(hats):
                return 1
            
            if idx < 0:
                return 0
            
            res = dp(mask, idx-1)
            for person in people[idx]:
                if mask&(1<<person) == 0:
                    res += dp(mask|(1<<person), idx-1)
                    
            return res%mod
        
        return dp()
                