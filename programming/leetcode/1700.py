class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]: 
                if neededTime[i+1] < neededTime[i]:
                    res += neededTime[i+1]
                    neededTime[i+1], neededTime[i] = neededTime[i], neededTime[i+1]             
                else:
                    res += neededTime[i]
                
        return res
                
                
        