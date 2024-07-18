class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        
        res = 0
        
        for value in counts.values():
            if value == 1:
                return -1
            cnt, rem = divmod(value, 3)
            if rem == 0:
                res += cnt
            else:
                res += cnt+1
                
        return res