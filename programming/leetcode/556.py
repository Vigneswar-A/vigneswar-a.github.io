class Solution:
    def nextGreaterElement(self, n: int) -> int:

        nums = list(map(int, str(n)))
        n = len(nums)

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        else:
            return -1

        k = i+1
        for j in range(i+1, n):
            if nums[j] > nums[i] and nums[j] < nums[k]:
                k = j

        nums[i], nums[k] = nums[k], nums[i]
        nums[i+1:] = sorted(nums[i+1:])

        res = int(''.join(map(str, nums)))
        return res if res < 2**31 else -1
        