class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        queue = deque(range(len(deck)))
        deck.sort()
        positions = []
        while queue:
            i = queue.popleft()
            positions.append(i)
            if queue:
                queue.append(queue.popleft())
            
        res = [0]*len(deck)
        
        for i,j in zip(positions, deck):
            res[i] = j
            
        return res