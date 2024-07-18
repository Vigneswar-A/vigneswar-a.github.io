
hashmap={'0':'0','1':'1','6':'9','8':'8','9':'6'}
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        rot=''
        for c in num:
            if c in hashmap:
                rot+=hashmap[c]
            else:
                return 0
            
        return rot[::-1]==num
            
        
        