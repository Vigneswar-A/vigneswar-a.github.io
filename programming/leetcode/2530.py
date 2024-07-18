class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
            
        def is_possible(target):
            aux = nums[:]
            
            for i in range(len(aux)-1,0,-1):
                if aux[i] > target:
                    aux[i-1] += aux[i]-target
                
                
            return aux[0] <= target
        
        return bisect.bisect_right(range(0, max(nums)+1), 0, key=is_possible)