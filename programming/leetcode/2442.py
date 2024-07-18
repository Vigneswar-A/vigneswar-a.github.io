class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        n = len(nums)
        count = 0
        hashset = set(nums)
        
        for i in nums:
            if i+diff in hashset and i+2*diff in hashset:
                count += 1       

        return count