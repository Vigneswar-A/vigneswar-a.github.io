class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i, n):
                flag = True
                prev = -inf
                for k in range(i):
                    if prev >= nums[k]:
                        flag = False
                        break
                    prev = nums[k]
                
                # if not flag:
                #     continue
                for k in range(j+1, n):
                    if prev >= nums[k]:
                        flag = False
                        break
                    prev = nums[k]

                res += flag
                
        return res
                
                
                
                        
                
            
                
        