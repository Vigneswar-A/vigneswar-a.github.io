class Solution:
    def countLetters(self, s: str) -> int:
        prev=s[0]
        count=total=0
        
        for c in s:
            
            if c==prev:
                count+=1
                
            else:
                total+=sum(range(1,count+1))
                count=1
                prev=c
                
        return total+sum(range(1,count+1))      