class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        prefix = set(words)
        for word in words:
            for k in range(1, len(word)):
                prefix.discard(word[k:])

        return sum(len(word) + 1 for word in prefix)
        