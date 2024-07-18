class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        wealth = Counter()
        
        for i in range(len(accounts)):
            for j in range(len(accounts[0])):
                wealth[i] += accounts[i][j]
                
        return max(wealth.values())