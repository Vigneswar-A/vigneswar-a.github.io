class Solution:
    def minInsertions(self, s: str) -> int:

        res = 0

        opens = 0
        closes = 0
        for c in s:
            if c == '(':
                if not closes:
                    opens += 1
                else:
                    res += 1
                    closes -= 1
            else:
                if opens:
                    closes += 1
                    if closes == 2:
                        opens -= 1
                        closes = 0
                else:
                    res += 1
                    opens = 1
                    closes = 1
            
        return res + (2*opens - closes)

            