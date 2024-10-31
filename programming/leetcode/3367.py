class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        res = 0
        for i in nums:
            res += int(str(max(map(int,str(i))))*len(str(i)))
        return res
        