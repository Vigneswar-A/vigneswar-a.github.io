class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum(dict((i,j) for j,i in enumerate(string.ascii_uppercase,1))[columnTitle[i]]*pow(26,len(columnTitle)-i-1) for i in range(0,len(columnTitle)))
            
        