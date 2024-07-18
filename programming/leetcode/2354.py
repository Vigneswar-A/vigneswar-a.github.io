class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        
        max_dmg = max(damage)
        if max_dmg < armor:
            return sum(damage) - max_dmg + 1
        else:
            return sum(damage) - armor + 1
    