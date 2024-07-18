class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {n:i for i,n in enumerate(nums)}
        
        for u,v in operations:
            nums[hashmap[u]] = v
            hashmap[v] = hashmap[u]
            del hashmap[u]
            
        return nums
        