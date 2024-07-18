class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        return len(re.findall(r'1+', s)) < 2
        