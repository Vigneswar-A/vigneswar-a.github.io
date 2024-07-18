class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        c = Counter(s)
        req = Counter("abc" * k)

        if req&c < req:
            return -1

        rem = c - req

        left = 0
        res = -inf

        for right in range(len(s)):
            rem[s[right]] -= 1
            while rem[s[right]] < 0:
                rem[s[left]] += 1
                left += 1
            res = max(res, right-left+1) 
        
        return len(s) - res


            

        
            