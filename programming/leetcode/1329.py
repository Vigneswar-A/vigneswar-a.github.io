class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        chips = Counter(position)
        to_odd = to_even = 0
        for pos,count in chips.items():
            if pos%2:
                to_even += count
            else:
                to_odd += count
                
        return min(to_odd , to_even)
            