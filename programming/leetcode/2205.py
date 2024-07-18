class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        n = len(security)
        good_days = [True]*n
        
        # condition 1
        for i in range(min(time, n)):
            good_days[i] = False
            good_days[-i-1] = False

        # condition 2
        count = 0
        for i in range(1, n):
            if security[i] <= security[i-1]:
                count += 1
            else:
                count = 0
            if count < time:
                good_days[i] = False

        # condition 3
        count = 0
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                count += 1
            else:
                count = 0
            if count < time:
                good_days[i] = False

        
        return [i for i in range(n) if good_days[i]]
                
