class Solution:
    def isValid(self, word: str) -> bool:
        return len(word) >= 3 and set(word) <= set(string.ascii_letters+string.digits) and any(c in word.lower() for c in 'aeiou') and any(c in word.lower() for c in 'bcdfghjklmnpqrstvwxyz')

        