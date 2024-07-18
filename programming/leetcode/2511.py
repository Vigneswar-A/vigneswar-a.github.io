class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        
        
        left = 0
        res = 0
        nums = []
        for i in range(1, len(s)):
            if int(s[left:i+1]) > k:
                nums.append(int(s[left:i]))
                left = i
                
        
        nums.append(int(s[left:]))
                
        for num in nums:
            if num > k:
                return -1
            
        return len(nums)
        