class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        
        
        values = [(i+j, idx) for idx,(i,j) in enumerate(zip(aliceValues, bobValues))]
        values.sort(reverse=1)
        
        ans = 0
        for i in range(len(values)):
            val = (aliceValues if i%2 == 0 else bobValues)[values[i][1]]
            if i%2 == 0:
                ans += val
            else:
                ans -= val
            
        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        else:
            return 0
            
        
        
        
        
        