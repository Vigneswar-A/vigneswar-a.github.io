class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse=1)
        return sum(max(0, happiness[i]-i) for i in range(k))
            
            
        