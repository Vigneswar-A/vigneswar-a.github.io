class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        
        if len(set(suits)) == 1:
            return "Flush"
        
        if any(count >= 3 for count in Counter(ranks).values()):
            return "Three of a Kind"
        
        if any(count >= 2 for count in Counter(ranks).values()):
            return "Pair"
        
        return "High Card"