class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        positive = {"X++", "++X"}
        
        res = 0
        
        for operation in operations:
            if operation in positive:
                res += 1
            else:
                res -= 1
                
        return res
        