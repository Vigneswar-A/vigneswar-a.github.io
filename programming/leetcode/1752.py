class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def is_arithmetic(arr):
            d = arr[1] - arr[0]
            for i in range(1, len(arr) - 1):
                if (arr[i+1] - arr[i]) != d:
                    return False
                
            return True
        
        res = []
        for l,r in zip(l,r):
            res.append(is_arithmetic(sorted(nums[l:r+1])))
            
        return res