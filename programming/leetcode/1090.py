class Solution:
    def isArmstrong(self, n: int) -> bool:
        return sum(map(lambda i:int(i)**len(string),(string:=str(n))))==n