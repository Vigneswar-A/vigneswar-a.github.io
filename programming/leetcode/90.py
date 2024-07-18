class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        temp = []
        for i in nums:
            temp = [arr + [i] for arr in res]
            res.extend(temp[:])

        return set(map(tuple , res))
            