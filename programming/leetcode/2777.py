class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        visited1 = set()
        visited2 = set()
        for i in range(len(nums)):
            visited1.add(nums[i])
            visited2.add(nums[-i-1])
            prefix.append(len(visited1))
            suffix.append(len(visited2))
        suffix.pop()
        suffix.reverse()
        
        return [i-j for i,j in zip(prefix, suffix)]+[len(visited2)]
            