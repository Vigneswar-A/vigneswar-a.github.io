class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        
        loses = Counter()
        for winner, loser in matches:
            loses[loser] += 1
            if winner not in loses:

                loses[winner] = 0
            
            
        zero,one = [],[]
        
        for player, lose in loses.items():
            if lose == 0:
                zero.append(player)
            elif lose == 1:
                one.append(player)
                
        zero.sort()
        one.sort()
        
        return [zero,one]
        
        
        
        
            
        
            
        