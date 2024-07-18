class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        new = [None] * len(nums)

        odd = 1
        even = 0
        
        for i in nums:
            if i%2:
                new[odd] = i
                odd += 2
            else:
                new[even] = i
                even += 2
        
        return new