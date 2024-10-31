class Solution:
    def minMaxDifference(self, num: int) -> int:
        nums = set()
        for i in range(10):
            for j in range(10):
                nums.add(int(str(num).replace(str(i), str(j))))
                
        maxv = max(nums)
        minv = min(nums)
        
        return maxv - minv
                
        