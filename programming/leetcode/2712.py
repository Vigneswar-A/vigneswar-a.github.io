class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        
        nums.sort()
        def is_impossible(k):
            if 2*k > len(nums):
                return True
            for i in range(k):
                if nums[i]*2 > nums[-(k-i)]:
                    return True
            return False
        
        return bisect_left(range(1, len(nums)), 1, key=is_impossible)*2
                    
                