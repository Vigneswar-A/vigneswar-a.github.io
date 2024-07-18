class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        s = set(aliceSizes)
        for bag in bobSizes:
            if bag + diff in s:
                return [bag + diff, bag]