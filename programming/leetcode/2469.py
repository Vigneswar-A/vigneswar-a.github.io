class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        prefix = list(accumulate(nums))
        return list(map(lambda i : bisect.bisect_right(prefix, i), queries))