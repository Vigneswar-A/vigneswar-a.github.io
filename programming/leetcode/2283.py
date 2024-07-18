class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd,even=sorted(nums[::2]),sorted(nums[1::2],reverse=1)
        return [i for array in itertools.zip_longest(odd,even) for i in array if i is not None]
        