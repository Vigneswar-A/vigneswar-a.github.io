class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dct=collections.Counter([x.lower() for x in licensePlate if x.isalpha()])
        return min([word for word in words if not dct-collections.Counter(word)], key=len)