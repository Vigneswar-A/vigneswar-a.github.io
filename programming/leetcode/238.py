class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        
        if zeros > 1: #if there are more than one zero then entire result is zero array
            return [0] * len(nums)
        
        prod = math.prod(filter(lambda n : n , nums))
        
        if zeros: #if there is one zero , all others are 0 other than the zero index itself
            
            i = nums.index(0)
            nums = [0] * len(nums)
            nums[i] = prod
            return nums
        
        else: #if no zeros just product by the number
            return [prod // i for i in nums]