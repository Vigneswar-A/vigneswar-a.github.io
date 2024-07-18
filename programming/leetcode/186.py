class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s.reverse()
        prev = 0
        for i in range(len(s)):
            if s[i] == " ":
                s[prev:i] = reversed(s[prev:i])
                prev = i+1               
        s[prev:] = reversed(s[prev:])
                
                
        
            
                    
                    
                
        
        