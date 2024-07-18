class Solution:
    def findNumbers(self, nums: List[int]) -> int:        
        count=0
        for n in nums:
            digits=0
            while n>0:
                n//=10;digits+=1
            count+=1-digits%2      
        return count
        
        
            