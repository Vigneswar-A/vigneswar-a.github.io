class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        def fix(i):
            if i == n:
                return
            temp = nums[i]
            fix(i+1)
            nums[(i+k)%n] = temp
            
        fix(0)
        
            
            