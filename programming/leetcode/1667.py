class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(1,n):
            s+=invert(s)
        return s[k-1]
    
def invert(s):
    output=""
    for i in s:
        output+="1" if i=="0" else "0"
    return '1'+output[::-1]
        
        