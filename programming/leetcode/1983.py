class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        minyear = float('inf')
        maxyear = -1
        
        for i , j in logs:
            minyear = min(i , minyear , j)
            maxyear = max(i , maxyear , j)
            
        maxcount = -1
        reqyear = 0

        for year in range(minyear , maxyear + 1):
            count = 0
            for birth , death in logs:
                if birth <= year < death:
                    count += 1
                    
            if count > maxcount:
                reqyear = year
                maxcount = count
            elif count == maxcount:
                reqyear = min(year, reqyear)
            
        return reqyear
        