class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)-2):
            substring=s[i:i+3]
            if substring[0]!=substring[1] and substring[0]!=substring[2] and substring[1]!=substring[2]:
                count+=1
        return count
            
            
        
        