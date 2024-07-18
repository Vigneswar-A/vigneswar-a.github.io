class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        mid = nums[len(nums)//2]
        
        smaller = []
        greater = []
        
        for i in nums:
            (smaller if i < mid else greater).append(i)
            
        nums.clear()
        for i in range(max(len(greater), len(smaller))):
            if i < len(greater):
                nums.append(greater[i])
            if i < len(smaller):
                nums.append(smaller[i])
            
            
        return nums