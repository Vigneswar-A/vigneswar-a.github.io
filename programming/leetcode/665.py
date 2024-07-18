class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if (n := len(nums)) == 1:
            return True
        
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                branch_1 = nums[:]
                branch_2 = nums[:]
                break
        else:
            return True
            
        
        branch_1[i] = branch_1[i - 1] if i else -float('inf')
        branch_2[i + 1] = branch_2[i + 2]  if i + 2 < n else float('inf')
        
        flag_1 = False
        flag_2 = False
        
        for i in range(i , n - 1):
            if branch_1[i + 1] < branch_1[i]:
                flag_1 = True
            if branch_2[i + 1] < branch_2[i]:
                flag_2 = True
        
        return not (flag_1 and flag_2)
                
                
                
        