class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        firstidx = [None]*26
        lastidx = [None]*26

        for i,c in enumerate(s):
            if firstidx[ord(c)-ord('a')] is None:
                firstidx[ord(c)-ord('a')] = i
            lastidx[ord(c)-ord('a')] = i

        res = 0
        for start,end in zip(firstidx, lastidx):
            if start != end != None:
                res += len(set(s[start+1:end]))

        return res
