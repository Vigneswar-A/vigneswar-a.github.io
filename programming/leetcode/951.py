class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        suffix = []
        val = nums[-1]
        for i in nums[::-1]:
            val = min(val, i)
            suffix.append(val)
        suffix.sort()
        print(suffix)
        val = nums[0]
        for i in range(len(nums)-1):
            val = max(val, nums[i])
            if val <= suffix[i+1]:
                return i+1
        return len(nums)-1
        
        
            
            
        
         
        