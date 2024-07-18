class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(i%2 for j,i in collections.Counter(s).items()) < 2
        