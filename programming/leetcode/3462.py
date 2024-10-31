class Solution:
    def doesAliceWin(self, s: str) -> bool:

        if any(c in 'aeiou' for c in s):
            return True
        return False
        