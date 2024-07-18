class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return re.match(r'(\d+?)0*$', num).group(1)
        