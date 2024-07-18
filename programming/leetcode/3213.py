class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        
        # number of subarrays where maximum element appears less than k times
        total = 0
        c = 0
        left = 0
        for right in range(n := len(nums)):
            if nums[right] == max_num:
                c += 1
                
            while c >= k:
                if nums[left] == max_num:
                    c -= 1
                left += 1
            length = right-left+1
            total += length
            
        total_sub_arrays = n*(n+1)//2
        return total_sub_arrays - total
        

        

            
            
            
        