from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        evens=isodd=0
        for n in Counter(s).values():
            evens+=n-n%2
            if not isodd and n%2:
                isodd=True
        return evens+isodd