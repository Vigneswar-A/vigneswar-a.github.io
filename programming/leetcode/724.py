class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0,*accumulate(nums)]

        for i in range(len(prefix) - 1):
            if prefix[i] + prefix[i + 1] == prefix[-1]:
                return i
            
        return -1

            