class Solution:
    def minTimeToType(self, word: str) -> int:
        
        time = 0
        currpos = 'a'
        
        for i in word:
            
            time += min(a:=abs(ord(i) - ord(currpos)) , 26 - a) + 1
            currpos = i
            
        return time        