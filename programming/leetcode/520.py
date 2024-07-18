import re
correct = re.compile(r'(^[A-Z]*$)|(^.[a-z]*$)').fullmatch
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return correct(word)
        