class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        s = str(num)
        count = 0
        for i in range(len(s) - k + 1):
            curr = int(s[i : i+k])
            if curr and  num % curr == 0:
                count += 1
        
        return count
                
        