class Solution:
    def findContestMatch(self, n: int) -> str:
        
        
        def recursion(teams):
            if len(teams) == 1:
                return teams[0]
        
            matches = []
            for i in range(len(teams)//2):
                matches.append('(' + teams[i] + ',' + teams[-i-1] + ')')
            return recursion(matches)
        
        
        return recursion(list(map(str, range(1, n+1))))
        
        
        