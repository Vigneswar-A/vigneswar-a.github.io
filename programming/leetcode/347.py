class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i,j in Counter(nums).most_common(k)]
        