class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
        res = 0
        for match in re.findall(r'0*1*', s):
            res = max(res, min(match.count('0'), match.count('1')))
            
        return res*2