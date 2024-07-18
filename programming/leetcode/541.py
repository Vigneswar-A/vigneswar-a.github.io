class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        for i in range(0, len(s), 2*k):
            s_list[i:i+k] = s_list[i+k-1:i-1 if i>0 else None:-1]
            
        return ''.join(s_list)
            
        