class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        nearest = -inf
        indices = set()
        for i in range(len(nums)):
            if nums[i] == key:
                nearest = i
            
            if i-nearest <= k:
                indices.add(i)

        nearest = inf
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == key:
                nearest = i
            
            if nearest-i <= k:
                indices.add(i)
                
        return sorted(indices)
        
            
        