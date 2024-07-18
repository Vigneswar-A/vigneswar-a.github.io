class Solution:
    def confusingNumber(self, n: int) -> bool:
        rev={'0':'0','1':'1','6':'9','8':'8','9':'6'}
        s=str(n)
        if any(d not in rev for d in s):
            return 
         
        return ''.join(map(rev.get,s[::-1]))!=s
        