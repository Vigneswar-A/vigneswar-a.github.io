class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        res = []
        
        for i in range(len(nums)//2):
            res.append(nums[i])
            res.append(nums[len(nums)//2 + i])
            
        return res
        