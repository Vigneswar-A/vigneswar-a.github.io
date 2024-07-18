class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:       
        return target <= jug1 + jug2 and target % gcd(jug1, jug2) == 0
        