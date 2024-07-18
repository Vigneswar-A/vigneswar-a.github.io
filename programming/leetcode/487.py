class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        flipped = False
        flip_num = 0
        
        left,right = 0,0
        size = len(nums)
        res = 0
        
        while right < size:
            if nums[right]:
                right += 1
            
            elif not flipped:
                flipped = True
                flip_num = right
                right += 1
                
            else:
                left = flip_num + 1
                flipped = False
            
            res = max(res , right - left)
                
        return res
                
            
                    
        