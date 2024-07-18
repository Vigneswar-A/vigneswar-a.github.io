from math import log,ceil
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound==0:return []
        List=[]
        for i in range(ceil(log(bound,x) if x!=1 else 1)):
            for j in range(ceil(log(bound,y) if y!=1 else 1)):
                if (num:=x**i+y**j)<=bound and num not in List: List.append(num)
        return List
        