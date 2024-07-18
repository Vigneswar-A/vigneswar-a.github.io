class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        n = len(potions)
        for spell in spells:
            req_potion = ceil(success/spell)
            num_potions = n-bisect.bisect_left(potions, req_potion)
            res.append(num_potions)
        return res
        