from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return (C:=Counter(moves))['U']==C['D'] and C['L']==C['R']