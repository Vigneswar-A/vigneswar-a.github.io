class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
        
        rewards = sorted(zip(reward1, reward2), key = lambda t : t[1]-t[0])
        return sum(rewards[i][i >= k] for i in range(len(reward1)))
            
            
        