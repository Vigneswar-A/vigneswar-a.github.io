class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        
        counts = Counter(hand)
        while counts:
            lowest = min(counts)
            for i in range(groupSize):
                counts[lowest+i] -= 1
                if counts[lowest+i] == 0:
                    del counts[lowest+i]
                elif counts[lowest+i] < 0:
                    return False
                    
        return True
                    
                