class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        path = []
        
        def backtrack(idx=0):
            if len(path) >= 2:
                res.add(tuple(path))
                
            for nxt in range(idx+1, len(nums)):
                if nums[nxt] >= nums[idx]:
                    path.append(nums[nxt])
                    backtrack(nxt)
                    path.pop()
             
        for i in range(len(nums)):
            path.append(nums[i])
            backtrack(i)
            path.pop()
                    
        return res
            
            
        