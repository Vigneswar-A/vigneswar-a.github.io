class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        nums = set(range(1, k+1))
        res = 0
        for i in rolls:
            nums.discard(i)
            if not nums:
                res += 1
                nums = set(range(1, k+1))
        return res+1
        
        