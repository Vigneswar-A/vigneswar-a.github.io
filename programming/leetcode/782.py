class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(collections.Counter(stones)[i] for i in jewels)