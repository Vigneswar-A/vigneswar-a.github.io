class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        res = delete = nodelete = -inf
        
        for i in range(len(arr)):
            nodelete, delete = max(nodelete+arr[i], arr[i]), max(nodelete, delete+arr[i])
            res = max(nodelete, delete, res)
            
        return res