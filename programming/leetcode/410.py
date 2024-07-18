class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(min_val):
            total = splits = 0
            for i in nums:
                if i > min_val:
                    return False
                if total+i > min_val:
                    total = 0
                    splits += 1
                total += i
                if splits+1 > k:
                    return False
            return True
        return bisect.bisect(range(sum(nums)), 0, key=lambda i : check(i))
        