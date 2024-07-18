class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [i for i,j in sorted(Counter(words).items(),key=lambda arr:(-arr[1],arr[0]))][:k]
        