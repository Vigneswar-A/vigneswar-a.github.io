class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        n = len(piles)
        def get_states(piles):
            piles = list(piles)
            for i in range(n):
                for j in range(1,piles[i]+1):
                    piles[i] -= j
                    yield tuple(piles)
                    piles[i] += j
        @cache
        def dp(state, maxplayer = True):
            if sum(state) == 0:
                return not maxplayer
            if maxplayer:
                score = -float('inf')
                for state in get_states(state):
                    if dp(state, False):
                        return True
                return False
            
            else:
                score = float('inf')
                for state in get_states(state):
                    if not dp(state , True):
                        return False
                return True
                
        return dp(tuple(piles))