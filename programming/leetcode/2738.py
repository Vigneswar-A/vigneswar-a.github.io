class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        
        s = set(nums)
        n = len(nums)
        res = 1
        visited = set()
        nums.sort()   
        for i in range(n):
            if nums[i] in visited:
                continue           
            start = current = nums[i]
            prev, curr = 1, 2
            while current+k in s:
                current += k
                visited.add(current)
                prev, curr = curr, prev+curr
            res *= curr

        return res
                    
                

        
            
            
            
        