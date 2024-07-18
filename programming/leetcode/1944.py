import re
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return re.search(r"(\b\w+(\b| ))"*k,s).group()
        