class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while (n := len(s)) > k:
            s = ''.join(str(sum(map(int , s[i : i + k]))) for i in range(0 , n , k))                        
        return s
        