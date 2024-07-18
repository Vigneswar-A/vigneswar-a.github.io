class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:   
        forbidden = set(forbidden)
        res = 0
        left = 0
        for right in range(len(word)):
            while any(word[i:right+1] in forbidden for i in range(max(left, right-10), right+1)):
                left += 1
            res = max(res, right-left+1)
        return res
                
                